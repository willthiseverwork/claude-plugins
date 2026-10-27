# App Review Intel

![App Review Intel logo](assets/logo.svg)

See what people love, hate and wish worked differently in apps they already use, with the App Store and Google Play reviews behind it. Use it to decide what to build, improve, test or say. Every finding shows the reviews it came from; a pattern in reviews is a lead to check, not proof of demand.

## Install in Claude Code

```text
/plugin marketplace add willthiseverwork/claude-plugins
/plugin install review-intelligence@willthiseverwork
```

Start a new Claude Code session after installation.

## How to use it

Paste or upload reviews and ask for a first useful read. If you have only an App Store or Google Play URL, use the [free Review Intel web tool](https://www.willthiseverwork.com/review-intel/?utm_source=github&utm_medium=referral&utm_content=free_plugin_readme), choose the storefront, export Markdown, and upload it to Claude.

- "Analyze this review export and find the strongest product, pricing, and ASO gaps."
- "Compare these two review exports and show which complaints recur."
- "Give me the full boring version."

The skill can use a separately connected Review Intel retrieval tool when one is available. This free package itself bundles no connector or server. For automatic pulls, see [Review Intel Pro](https://github.com/willthiseverwork/review-intelligence/tree/main/plugins/review-intel-pro).

## What is inside

The `app-review-growth-analyzer` skill includes the Review Intelligence v13 method: core rules, evidence protocol, conversation modes, the full report format and worked examples. The earlier v12 prompt is kept as a regression baseline.

Major findings carry stable review IDs and short quotes. Percentages use the reviews actually analyzed. Inferences stay separate from what reviewers said, and suggested language includes what not to claim.

## Data and privacy

Reviews you paste or upload are analyzed in your Claude conversation under your Claude account's terms and privacy settings. This package contains no server configuration. If you separately connect a retrieval service, that service's privacy terms also apply.

- [Privacy](https://www.willthiseverwork.com/review-intel/privacy/)
- [Support](https://www.willthiseverwork.com/review-intel/support/)
- [Terms](https://www.willthiseverwork.com/review-intel/terms/)

## Limits

Reviews show patterns in the analyzed sample. They do not prove revenue, retention, conversion, causality or what every user thinks. Review Intel is not affiliated with or endorsed by Apple or Google.

## License

Apache License 2.0. See [LICENSE](LICENSE).
