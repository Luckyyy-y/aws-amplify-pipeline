#!/usr/bin/env bash
set -euo pipefail

# Run from the repository root so local and Amplify checks use the same files.
cd "$(dirname "$0")/.."

echo "CHECK 1 of 3 - page must have a nonempty title"
if [[ ! -f index.html ]] || ! grep -Eqi '<title>[^<]*[^[:space:]<][^<]*</title>' index.html; then
  echo "FAILED - index.html needs a nonempty title on one line."
  exit 1
fi

echo "CHECK 2 of 3 - page must include Gerardo Vera"
if ! grep -Fq 'Gerardo Vera' index.html; then
  echo "FAILED - the page is missing Gerardo Vera."
  exit 1
fi

echo "CHECK 3 of 3 - no AWS access key ID patterns in text files"
# -l prints only filenames, so a possible credential is not repeated in logs.
# Scan documentation too. Skip git history, generated Python files, and images.
scan_status=0
grep -rIlE '(AKIA|ASIA)[0-9A-Z]{16}' \
  --exclude-dir=.git --exclude-dir=__pycache__ \
  --exclude-dir=.sites-runtime --exclude-dir=images . || scan_status=$?
if [[ "$scan_status" -eq 0 ]]; then
  echo "FAILED - an AWS access key ID pattern was found. Check the files listed above."
  exit 1
elif [[ "$scan_status" -ne 1 ]]; then
  echo "FAILED - the scan could not complete."
  exit 1
fi

echo "ALL CHECKS PASSED"
