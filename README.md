# Boardroom

[![Validate skill](https://github.com/YOUR-USERNAME/boardroom/actions/workflows/validate.yml/badge.svg)](https://github.com/YOUR-USERNAME/boardroom/actions/workflows/validate.yml)

A Claude skill that runs a business decision through a panel of distinct expert lenses, grounded in real research and in the numbers only you know, then cross-examines the panel to force one clear recommendation instead of a pile of hedged opinions.

> Swap `YOUR-USERNAME` in the badge link above once this is pushed to your own GitHub account.

## Why this exists

Ask an AI "what do you think of this idea" and you tend to get generic, hedge-everything advice. Run a SWOT and you get a list of pros and cons that never actually resolves into a decision. Boardroom does two things differently: every lens answers one narrow question instead of "give me your thoughts," and a final cross-examination step forces those separate views into a single, defensible call instead of leaving you to weigh four opinions yourself.

It's grounded on purpose. Before any lens speaks, it researches what's actually true about your specific situation and asks you for the operational numbers only you know (current revenue, staff costs, marketing budget, whatever the decision needs). An opinion built purely from a model's memory is just a prior dressed up as analysis.

## How it works

1. **Restate the decision and confirm the lineup.** Refuses to guess at a vague decision, and tells you upfront which lenses are active before doing anything else.
2. **Gather evidence.** External facts get researched and cited. Internal facts (yours to know, not to guess) get asked for directly, in one short batch.
3. **Run the panel.** CEO, COO, PM, and Founder run every time, each answering a deliberately narrow question. CFO, HR, or Marketing join on top when the decision actually calls for them.
4. **Cross-examine.** Not a fifth opinion, a stress test of the four verdicts against the evidence, looking for contradictions and unsupported confidence.
5. **Final call.** One recommendation, a confidence score with the reasoning attached, and what would need to change to flip it.

## Example

**Prompt:** "Should we switch card payment processors to cut fees?"

> **Active lenses:** the core four, plus CFO. Not HR, a short device walkthrough for two till operators isn't a staffing decision. Not Marketing, customers don't know or care which processor runs behind the till.
>
> **Quick answer:** Yes, switching saves roughly R1,205/month (about 36%) at current turnover, with low operational risk. Confidence 4/5.
>
> CFO: current cost at 2.75% on R120,000 monthly turnover is R3,300. The provider being considered publishes a real rate of 2.30% up to R50k and 1.35% above that, working out to R2,095/month, a sourced figure, not an estimate. CEO, COO, PM, and Founder all agreed with only a minor operational note (a short reconciliation window while switching machines), which PM's suggested cutover plan already covers.
>
> **Why 4/5, not 5:** the saving is based on today's turnover mix and the new provider's published rate, not a full market comparison or confirmation there's no early-termination cost with the current provider.

## Guardrails

- No lens is ever a named real person. Roles are archetypes, not impersonations, so nothing gets attributed to someone who never said it.
- A confidence score never appears without the reasoning behind it attached.
- Evidence gaps, whether from research or from you, get named honestly instead of papered over with a plausible guess.

## Install

This ships as a Claude skill, a `SKILL.md` file packaged inside `boardroom.skill` (a plain zip). Unzip it and drop the `boardroom` folder into your skills directory. In Claude Code that's typically `.claude/skills/`. In apps that support uploading a `.skill` file directly, use that instead. Once installed, it triggers on business decision questions without needing to be named explicitly, though saying "run this through the boardroom" also works.

## Extending it

Add a new lens by giving it a name, a one-line description of what it does and doesn't care about, a narrow question it answers, and a note on what internal evidence it needs from you. Full detail is in `SKILL.md` under "Extending this," and in [CONTRIBUTING.md](CONTRIBUTING.md) if you're planning to open a pull request.

## More examples and tests

Four full transcripts, covering a staffing-and-compliance-heavy decision, a finance-heavy decision, a low-stakes decision where the panel genuinely agreed instead of manufacturing a disagreement, and a deliberately vague prompt, are in [`examples/`](examples/). The prompts and expected behavior behind them are in [`evals/evals.json`](evals/evals.json). [`CHANGELOG.md`](CHANGELOG.md) has the version history and what each version fixed.

## Repo layout

```
SKILL.md                     the skill itself
README.md                    this file
CHANGELOG.md                 version history
CONTRIBUTING.md              how to add a lens
LICENSE                      MIT
examples/                    full run transcripts
evals/evals.json             test prompts and expected behavior
scripts/validate_skill.py    frontmatter validator, also runs in CI
.github/workflows/validate.yml
```

## License

MIT, see [LICENSE](LICENSE).
