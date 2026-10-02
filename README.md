# Period Care Bills Tracker

Live site: **[https://edmundmiller.github.io/periodic_legislation/](https://edmundmiller.github.io/periodic_legislation/)**

The previous Evidence Cloud homepage is still at [https://getperiodic.evidence.app](https://getperiodic.evidence.app). That host is not updated by this repo’s pipeline.

## Deployment

The daily workflow (`.github/workflows/run-pipeline.yml`) refreshes LegiScan data **in the runner**, builds the Evidence static site (`npm run sources` + `npm run build`), and deploys the `build/` output to GitHub Pages.

It does **not** commit generated CSVs or site files back to `main` (or any other branch). After merge, the midnight job can refresh the site without a new commit on the contribution graph.

### Enable GitHub Pages (one-time, required)

1. Open the repo **Settings → Pages**
2. Set **Source** to **GitHub Actions** (not “Deploy from a branch”)
3. After the first successful `Run Pipeline Daily` run, the site is at `https://edmundmiller.github.io/periodic_legislation/`

Pages uses the default `GITHUB_TOKEN` with `pages: write` and `id-token: write`. No extra deploy secrets. The pipeline still needs `secrets.LEGISCAN_APIKEY` for the LegiScan fetch.

### Summaries workflow

`.github/workflows/run-summaries.yml` is dispatch-only (the monthly schedule is commented out). It no longer auto-commits. Generated `sources/generated/state_period_care_vibes.csv` is uploaded as a workflow artifact; commit it via a PR if you want it persisted for later builds.

# Evidence Template Project

## Using Codespaces

If you are using this template in Codespaces, click the `Start Evidence` button in the bottom status bar. This will install dependencies and open a preview of your project in your browser - you should get a popup prompting you to open in browser.

Or you can use the following commands to get started:

```bash
npm install
npm run sources
npm run dev -- --host 0.0.0.0
```

See [the CLI docs](https://docs.evidence.dev/cli/) for more command information.

**Note:** Codespaces is much faster on the Desktop app. After the Codespace has booted, select the hamburger menu → Open in VS Code Desktop.

## Get Started from VS Code

The easiest way to get started is using the [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=Evidence.evidence-vscode):



1. Install the extension from the VS Code Marketplace
2. Open the Command Palette (Ctrl/Cmd + Shift + P) and enter `Evidence: New Evidence Project`
3. Click `Start Evidence` in the bottom status bar

## Get Started using the CLI

```bash
npx degit evidence-dev/template my-project
cd my-project 
npm install 
npm run sources
npm run dev 
```

Check out the docs for [alternative install methods](https://docs.evidence.dev/getting-started/install-evidence) including Docker, Github Codespaces, and alongside dbt.



## Learning More

- [Docs](https://docs.evidence.dev/)
- [Github](https://github.com/evidence-dev/evidence)
- [Slack Community](https://slack.evidence.dev/)
- [Evidence Home Page](https://www.evidence.dev)
