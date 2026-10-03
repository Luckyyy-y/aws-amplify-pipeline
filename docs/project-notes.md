# Project notes

## The problem

A small website can still be published with something missing or with a credential accidentally pasted into a file. This lab gives me a way to see how checks can stop a build before publication.

## Starting point

The club starter had three files. Its build checked for a title tag and an AWS access key ID pattern. It also included workshop instructions for deliberately failing the build.

## Changes in this copy

| Change | Reason |
| --- | --- |
| Personalized the HTML page | Give the lab a clear purpose and show the actual project status |
| Moved checks into `scripts/check.sh` | Use one command locally, in GitHub Actions, and in Amplify |
| Checked for a nonempty title | An empty title should fail too |
| Added the Gerardo Vera check | Practice writing an additional content check |
| Included documentation in the key scan | A key in a README is still a key in the repository |
| Added the `ASIA` pattern | Practice recognizing temporary access key IDs as well |
| Printed filenames instead of matches | Avoid repeating a possible credential in the build log |
| Added isolated failure-case tests | Check that the build script actually rejects the intended mistakes |

## Verified locally

The check script passed on the real page. All nine tests passed:

| Example | Expected result | Local result |
| --- | --- | --- |
| Valid page | Pass | Pass |
| Missing page | Block | Blocked |
| Missing title | Block | Blocked |
| Blank title | Block | Blocked |
| Missing name | Block | Blocked |
| Fake key ID in HTML | Block without printing the ID | Blocked; ID absent from log |
| Fake key ID in README | Block | Blocked |
| Temporary key ID pattern in another text file | Block | Blocked |
| Fake fixture inside `.git` | Exclude Git metadata | Excluded |

The fake IDs are generated inside temporary test folders. They are not real credentials, and the tests do not commit a broken version of the page.

## Still to verify

These results show that the local script works for these examples. They do not show that Amplify has deployed anything or preserved the previous site after a failed build. That evidence belongs in [deployment.md](deployment.md) after testing on AWS.

## Notes to add after doing the AWS lab

- What happened during the first build?
- Which log message helped diagnose a failure?
- Did the old version remain online when a build failed?
- What would I change about these basic checks?

These questions are unfinished notes, not a claim that I have already completed the deployment.
