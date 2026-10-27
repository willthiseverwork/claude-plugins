# ASO Keyword Sorter

![ASO Keyword Sorter icon](assets/icon.svg)

Sort a raw keyword list into App Store listing candidates, content topics and keywords to drop, with the reason for each. Every keyword comes back exactly as you gave it, and unclear ones stay visible instead of disappearing. It doesn't fetch search volume, rankings or live store data.

## Install in Claude Code

```text
/plugin marketplace add willthiseverwork/claude-plugins
/plugin install aso-keyword-intent@willthiseverwork
```

Start a new Claude Code session after installation.

## What it does

- Classify App Store intent
- Identify content-planning queries
- Preserve raw keyword exports

Every keyword you supply comes back unchanged in an eight-column table: `Keyword`, `Label`, `Confidence`, `Segment`, `Metadata_action`, `Strip_words`, `Content_cluster` and `Reason`. Each phrase is labelled `app_search`, `informational`, `ambiguous` or `out_of_category`, followed by a short bucket count and pattern summary.

## How to use it

Paste your keyword list together with a one-line description of your app and any features it does not have. Claude asks once for the app description if it is missing. For example:

- "Classify these keywords for my Spanish-learning app: short daily lessons, no French or live tutors."
- "Use this keyword export to separate App Store metadata candidates from SEO content topics for my habit-tracking app."
- "Classify these phrases without changing the original keywords."

## What is inside

- The `aso-keyword-intent` skill with its v4 classification rubric in Markdown. The original locked RTF rubric is kept beside it for provenance and checksum verification.
- Two optional helper scripts, `prepare_input.py` and `validate_output.py`. Where your Claude environment can run code, Claude may use them on a CSV you provide to keep only the keyword column and to check that the result has all eight columns. They read and write local files only and make no network requests.

## Data and privacy

The plugin is instructions only. It has no server, connector, account, database or telemetry, and it sends nothing to Will This Ever Work. Claude processes the keywords and app context you provide under your Claude account's terms and privacy settings. Share only information you are entitled to share.

Privacy notice and support: https://www.willthiseverwork.com/plugins/privacy/ (support email: support@willthiseverwork.com).

## Limits

A metadata candidate is a research candidate, not a ranking, volume, conversion or policy claim. The plugin does not access an app-store account, edit metadata, publish content or submit a listing.

## License

Apache License 2.0. See [LICENSE](LICENSE).
