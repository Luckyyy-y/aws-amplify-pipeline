# AWS deployment checklist

**Not completed yet.** This is the next part of the lab. Do not mark steps done until the result is visible on the AWS account.

## Connect the repository

1. Check your AWS plan, Amplify pricing, and billing alerts before creating an app. This README does not promise free hosting.
2. In Amplify Hosting, start a new app using GitHub as the source.
3. Select `Luckyyy-y/aws-amplify-pipeline` and the `main` branch. Limit the GitHub app's access to this repository when configuring it.
4. Confirm the build settings use this repository's `amplify.yml`. The build runs `bash scripts/check.sh`; the published artifact is `index.html` from the repository root.
5. Deploy, then open the supplied Amplify URL and confirm the page loads.
6. Record the actual URL, commit, and build result below. Do not put passwords, access keys, account IDs, or other private console details in screenshots.

## Verify updates and failures

After the first deployment:

- Make a harmless sentence change, commit it, and verify that Amplify automatically publishes that version.
- Remove the title on a temporary test branch. Connect that branch for testing if your AWS setup allows it, then verify the build fails. Restore the title afterward.
- To prove the *last working version stays online*, test a good build and then a bad build on the same Amplify branch. Record both commit IDs and check the branch URL after the failure.
- Use only generated fake IDs if testing the key check. Never use a real AWS credential for an exercise.
- Restore a valid page and confirm the next deployment passes.

GitHub Actions also checks the code, but it cannot substitute for these AWS observations.

## Evidence to fill in

| Evidence | Result |
| --- | --- |
| Live Amplify URL | Not available yet |
| First deployed commit | Not recorded yet |
| Automatic update | Not verified yet |
| Failed title build log | Not recorded yet |
| Failed fake-key build log | Not recorded yet |
| Previous page after a failed build | Not verified yet |
| Recovery deployment | Not verified yet |

Save relevant screenshots under `docs/images/` and link them here with a sentence explaining what each screenshot proves. A short video can be added later.

## References

- [Original club workshop](https://github.com/uhawscloudclub/pipeline-starter-aws)
- [AWS Amplify build specification](https://docs.aws.amazon.com/amplify/latest/userguide/yml-specification-syntax.html)
- [AWS Amplify pricing](https://aws.amazon.com/amplify/pricing/)
- [GitHub Actions workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)

If the app is only for practice, delete the unused Amplify app when finished and review the billing console. Keeping a repository on GitHub does not require keeping an AWS app running.
