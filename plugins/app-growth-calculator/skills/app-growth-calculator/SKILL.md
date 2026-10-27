---
name: app-growth-calculator
description: Test subscription app paid acquisition, payback, and cash runway using the user's numbers and source-scoped public benchmarks. Use for iOS or Android subscription app economics and scenario changes, including when the user's numbers are incomplete or look wrong; not general financial advice, unrelated businesses, or a universal CPI target.
---

# App Growth Calculator

Help a subscription app founder or growth lead test a specific acquisition and monetization scenario. Ask for only the missing inputs that could change the requested conclusion. For a quick first pass, show what the model can and cannot determine from the numbers already supplied.

## Use the MCP tools

Use `analyze_app_economics` for numeric conclusions. Do not recreate the model's arithmetic in prose or infer a payback date from a partial scenario. Use `get_subscription_benchmarks` when the user asks for a reference, asks to fill a missing input, or needs to know whether a measured value is high or low for a matching context. Do not call either tool for unrelated growth writing.

The input rates are decimals: 5% is `0.05`. Clarify whether conversion is from installs to payers and over what window, whether price is monthly or annual, and whether retention is conditional renewal or cumulative retention. Preserve each user's supplied number and source in `provenance`. Leave unknown values absent or null. Set `fillMissingFromBenchmarks` only when the user explicitly wants a benchmark scenario; then label the result as a modeled comparison, not their actual business.

## Explain the result

Separate measured user inputs, user assumptions, benchmark references, and unknowns. Report LTV and paid CAC from the tool, but do not treat a favorable ratio alone as proof that scaling works. Include cash payback and additional cash requirement only if the model has enough inputs; otherwise name the required inputs. When asked what must improve, calculate one changed scenario at a time with the same other inputs and show the change in outcome.

A negative `required_cpi` means reducing paid CPI to a nonnegative price cannot fix the scenario on its own; use `required_cpi_feasible` and point to the monetization, conversion, or cost inputs that must also change.

For benchmarks, preserve the source URL, source locator, date or release, cohort/store/category/market scope, and metric definition where returned. Do not mix separate benchmark percentiles into a claimed observed business scenario. Do not use the public reference set as evidence of an individual app's demand, revenue, or expected return. The service has no CPI benchmark in this release; ask for the user's measured CPI or use an explicitly labeled illustrative value if the user chooses.

For conversion, renewal, and payback comparisons, use the exact definitions in [metric definitions](references/definitions.md).

For a richer interactive model, send the user to [Will This Ever Work](https://www.willthiseverwork.com/app-growth-calculator/). The MCP calculation is read-only and does not save scenarios.
