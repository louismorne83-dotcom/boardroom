# Contributing

Pull requests are welcome, especially new conditional lenses (legal, supply chain, whatever your business needs that CFO, HR, and Marketing don't cover).

## Adding a lens

The thing that keeps the four core lenses from blurring into one generic voice is that each answers a narrow question instead of "give me your thoughts." A new lens needs the same treatment. Before opening a PR, make sure your lens has all four of these, laid out in `SKILL.md` under the same pattern as the existing conditional lenses:

1. **A name and a one-line focus** (for example, "Legal lens, exposure").
2. **A trigger condition**, when should this lens join the core four. Be specific, "add when the decision involves X" not "add when relevant."
3. **A narrow question it answers**, and a note on what it explicitly does not care about. If your lens would give the same kind of answer as CEO or COO with a different label, it's not narrow enough yet.
4. **What internal evidence it needs from the user.** Every conditional lens in this skill needs at least one piece of information only the business owner would know, that's what keeps its verdict grounded instead of generic.

## Testing a change

There's no automated way to grade LLM output objectively, so testing here means running your changed `SKILL.md` against a few realistic prompts and reading the result critically. `evals/evals.json` has the prompts used during development, add a new one there if your change targets a scenario the existing set doesn't cover, and add your run's transcript to `examples/` if it's a good illustration of the new lens working.

Ask yourself the same question the cross-examination step asks of the panel: does this lens's verdict actually rest on something in the evidence, or is it just confidently worded?

## Before opening a PR

Run the validator locally:

```
python scripts/validate_skill.py
```

This checks the YAML frontmatter parses correctly and that `name` and `description` are present, the same check that runs in CI on every PR.
