"""Try the real check script against temporary copies, not the working page."""
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class BuildChecksTest(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.project = Path(self.folder.name)
        (self.project / "scripts").mkdir()
        shutil.copy(ROOT / "scripts/check.sh", self.project / "scripts/check.sh")
        self.page = self.project / "index.html"
        self.page.write_text("<title>Pipeline Lab</title>\n<h1>Gerardo Vera</h1>\n")

    def run_checks(self):
        return subprocess.run(
            ["bash", str(self.project / "scripts/check.sh")],
            capture_output=True, text=True, check=False,
        )

    def test_valid_page_passes(self):
        result = self.run_checks()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_page_fails(self):
        self.page.unlink()
        self.assertNotEqual(self.run_checks().returncode, 0)

    def test_missing_title_fails(self):
        self.page.write_text("<h1>Gerardo Vera</h1>")
        self.assertNotEqual(self.run_checks().returncode, 0)

    def test_blank_title_fails(self):
        self.page.write_text("<title>   </title>\nGerardo Vera")
        self.assertNotEqual(self.run_checks().returncode, 0)

    def test_missing_name_fails(self):
        self.page.write_text("<title>Pipeline Lab</title>")
        self.assertNotEqual(self.run_checks().returncode, 0)

    def test_fake_key_in_page_fails_without_printing_key(self):
        fake_key = "AKIA" + "0" * 16  # Generated test data, not a credential.
        with self.page.open("a") as file:
            file.write(fake_key)
        result = self.run_checks()
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn(fake_key, result.stdout + result.stderr)

    def test_fake_key_in_readme_fails(self):
        (self.project / "README.md").write_text("AKIA" + "0" * 16)
        self.assertNotEqual(self.run_checks().returncode, 0)

    def test_temporary_key_id_pattern_fails(self):
        (self.project / "notes.txt").write_text("ASIA" + "0" * 16)
        self.assertNotEqual(self.run_checks().returncode, 0)

    def test_git_history_folder_is_excluded(self):
        (self.project / ".git").mkdir()
        (self.project / ".git/test-fixture").write_text("AKIA" + "0" * 16)
        self.assertEqual(self.run_checks().returncode, 0)


if __name__ == "__main__":
    unittest.main()
