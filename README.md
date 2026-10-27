# Will This Ever Work plugins

Claude plugins published by [Will This Ever Work](https://www.willthiseverwork.com/?utm_source=github&utm_medium=referral&utm_content=plugins_readme), created by Dasha Antonova.

## Install in Claude Code

Add the marketplace once:

```text
/plugin marketplace add willthiseverwork/claude-plugins
```

Then install the plugins you want:

| Plugin | What it does | Install command |
| --- | --- | --- |
| [ASO Keyword Sorter](plugins/aso-keyword-intent) | Sort keywords into App Store candidates, content topics and terms to drop. | `/plugin install aso-keyword-intent@willthiseverwork` |
| [Job Interview Story Coach](plugins/interview-story-coach) | Build truthful interview stories and practise for a role. | `/plugin install interview-story-coach@willthiseverwork` |
| [Make My Product Clear](plugins/make-my-product-clear) | Rewrite product copy so customers understand its value and next step. | `/plugin install make-my-product-clear@willthiseverwork` |
| [App Growth Calculator](plugins/app-growth-calculator) | Test subscription-app payback and cash assumptions. | `/plugin install app-growth-calculator@willthiseverwork` |
| [App Review Intel](plugins/review-intelligence) | Analyze reviews you paste or upload, including free Review Intel exports. | `/plugin install review-intelligence@willthiseverwork` |
| [Directories Done](plugins/directories-done) | Prepare, approve, submit and verify free directory listings. | `/plugin install directories-done@willthiseverwork` |

Start a new Claude Code session after installation. The marketplace name is `willthiseverwork`; plugin IDs remain unchanged.

Five packages contain skills only. App Growth Calculator also includes its hosted, read-only calculator connector. App Review Intel includes no server; see its README for the export-and-upload workflow.

## Review Intel Pro

For automatic app-review retrieval through the signed-in connector, install [Review Intel Pro](https://github.com/willthiseverwork/review-intelligence/tree/main/plugins/review-intel-pro) from its separate marketplace:

```text
/plugin marketplace add willthiseverwork/review-intelligence
/plugin install review-intel-pro@review-intel
```

That repository also retains the Codex and ChatGPT package. Pro access is determined by the hosted Review Intel service.

## Licenses

Each plugin includes its own license. ASO Keyword Sorter, Job Interview Story Coach, Make My Product Clear, App Growth Calculator and App Review Intel use Apache-2.0. Directories Done uses its included proprietary license; it is available to install and use under those terms.
