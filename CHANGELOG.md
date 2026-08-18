# Changelog

## v1

- Initial release. Four core lenses (CEO, COO, PM, Founder), each answering a narrow question instead of giving a general opinion.
- Research step grounds every run in real, cited evidence instead of the model's memory.
- Cross-examination step stress-tests the panel's verdicts against each other and against the evidence before producing one final call.
- Guardrail against roleplaying named real people, lenses stay role-based archetypes.

## v2

- Added CFO, HR, and Marketing as conditional lenses that join only when the decision calls for them, instead of running every lens on every decision.
- Added the "internal evidence" half of the research step: the skill now asks the user directly for operational numbers only they would know (current revenue, staff costs, marketing budget, trading hours), batched into one short set of questions, rather than only pulling external, web-findable facts.
- Evidence Snapshot in the output template split into "from you" and "from research," so it's always clear where a fact came from.

## v3

- Added a one-line "Quick answer" headline at the top of the output, so the recommendation and confidence score are visible without reading the full breakdown.
- Active lenses are now surfaced immediately after the decision is restated, before evidence gathering starts, instead of only becoming visible in the final output. This gives the option to correct a wrong or missing lens before the rest of the run builds on top of it.

Tested across four scenarios during development: a staffing-and-compliance-heavy decision (surfaced a real, previously-missed legal cost), a finance-heavy decision (caught a real internal contradiction between two lenses), a low-stakes decision where the panel genuinely agreed (confirmed the cross-examination step doesn't manufacture disagreement that isn't there), and a deliberately vague prompt (confirmed the skill asks for specifics instead of guessing at the decision). See `examples/` for the full transcripts.
