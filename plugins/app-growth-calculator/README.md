# App Growth Calculator

![App Growth Calculator icon](assets/icon.svg)

Enter your subscription app's acquisition, conversion, pricing, retention, spend, and cash assumptions. See whether paid growth covers acquisition cost, when cash pays back, and which input changes the answer. Reviewed public benchmarks include source links, definitions, and scope; missing inputs stay unknown.

## Install in Claude Code

```text
/plugin marketplace add willthiseverwork/claude-plugins
/plugin install app-growth-calculator@willthiseverwork
```

Start a new Claude Code session after installation.

## What it does

- Calculate app economics
- Get benchmark context

Claude uses the calculator's tools for every numeric conclusion instead of doing the arithmetic in prose. Results keep earned payback (LTV against paid CAC) separate from cash payback, label each input as measured, assumed, benchmark or unknown, and name the missing inputs when a conclusion cannot be reached.

## How to use it

Add the plugin, then open its Connectors tab on claude.ai or in Cowork and connect `app-growth-calculator`. No account or sign-in is needed. Claude Code connects to it directly. Then ask, for example:

- "We pay $3 per install and 5% become paying subscribers. What else do you need to test payback?"
- "Can my subscription app fund the wait for paid acquisition to pay back?"
- "Which input has to improve for this acquisition plan to work?"

For a richer interactive model, use the browser calculators at https://www.willthiseverwork.com/app-growth-calculator/.

## What is inside

- The `app-growth-calculator` skill, with metric definitions for conversion, first annual renewal, payer value and cash payback.
- A remote MCP connector: `https://www.willthiseverwork.com/app-growth-calculator/mcp`. It has two read-only tools: `analyze_app_economics` (unit economics and a 24-month cash forecast from your inputs) and `get_subscription_benchmarks` (reviewed public benchmark records with definitions, scope and source links).

## Data and privacy

When Claude calls a tool, the calculator server receives that tool call: the commercial inputs you give (such as price, acquisition cost, conversion, retention, fees, refunds, budget and timing), an optional scenario name and provenance notes, and the benchmark context. It processes them in memory to return the result. It does not create an account, use an application database or save scenarios. The server is hosted on Vercel; customer-accessible runtime logs are kept for one hour. Do not put personal, confidential or sensitive information in scenario names or notes. Claude processes your conversation under your Claude account's terms and privacy settings.

- Privacy: https://www.willthiseverwork.com/app-growth-calculator/privacy/
- Support: https://www.willthiseverwork.com/app-growth-calculator/support/ (support@willthiseverwork.com)
- Terms: https://www.willthiseverwork.com/app-growth-calculator/terms/

## Limits

Not financial advice. Built for iOS and Android subscription apps; it does not model other businesses or give a universal CPI target. This release has no CPI benchmark, and benchmark records are public references with stated scope, not evidence of an individual app's demand, revenue or return.

## License

Apache License 2.0. See [LICENSE](LICENSE).
