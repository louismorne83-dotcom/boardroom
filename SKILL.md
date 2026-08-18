---
name: boardroom
description: >
  Runs a business decision or idea through a panel of distinct expert lenses (CEO, COO, PM, Founder,
  plus CFO, HR, or Marketing when the decision calls for them), grounded in real researched evidence
  and in operational numbers it asks the user for (current revenue, staff costs, marketing budget,
  trading hours, whatever's actually needed), then cross-examines their verdicts to produce one clear
  recommendation with a confidence score and named risks. Use this whenever someone wants to
  stress-test a business decision before committing to it, for example a pricing change, a new
  product or market move, a hiring or staffing call, an operational change, a marketing spend, a
  supplier decision, or any "should we do X" question. Also trigger on phrases like "run this through
  the boardroom", "what would the panel say", "is this a good idea", "sanity check this decision", or
  "I want a second opinion on this", even if the user doesn't name the skill directly. Works for any
  business or industry, not just one sector.
---

# Boardroom

## What this is

A structured way to pressure-test a business decision before money or time gets committed to it. Instead of one voice giving one opinion, four distinct roles evaluate the decision through four different, deliberately narrow lenses, using evidence gathered specifically for the question at hand. A fifth step cross-examines what the four roles said and forces one final call.

The point of the narrow lenses is that a single generic "give me your thoughts on this idea" prompt tends to produce generic, hedge-everything advice. Forcing each role to answer only its own question, using only the shared evidence, is what keeps the output sharp and stops the four voices from blurring into one.

## The process

Follow these steps in order. Don't skip the research step, even if the topic feels familiar, and don't let the roles see each other's verdicts until the cross-examination step.

### Step 1: Restate the decision and confirm the lineup

In one or two sentences, state exactly what is being decided. If the user's question is vague ("should we expand?"), ask what specifically is being considered before going further, since the whole exercise only works if the decision is concrete.

Then decide which roles are active for this one. The four core roles (CEO, COO, PM, Founder) always run, see Step 3 for when CFO, HR, or Marketing join on top. Say the lineup out loud before doing anything else, for example "Active lenses for this one: the core four, plus HR and Marketing." Do this before evidence gathering, not after, so the user can correct it if a lens looks wrong or missing before the rest of the run builds on top of it.

### Step 2: Gather evidence

Evidence comes from two places, and they need different handling.

**External evidence** is anything findable independently: market data, competitor behavior, regulatory context, industry benchmarks, seasonal patterns. Research this using web search or any other data source available, and cite sources. This exists because an opinion generated purely from memory is just the model's prior dressed up as analysis, a real evaluation needs facts that are current and specific to the question, not general knowledge about the topic.

**Internal evidence** is anything only the person running this actually knows: current trading hours, current revenue or sales figures, staff costs and overtime rates, existing marketing budget, whether promotional material already exists, headcount, current pricing, whatever the roles active for this decision (see Step 3) actually need to give a grounded answer. Don't guess at these. Work out what's needed from the active roles, then ask for it directly in one short, specific, batched set of questions, not a generic intake form and not one question at a time. Only ask for what this particular decision needs.

If the user doesn't have a number on hand, don't stall on it, proceed and name it as a gap in the Evidence Snapshot instead. A named gap is more useful than a confident invention, whether that invention would have come from research or from guessing at the user's numbers.

### Step 3: Run the panel

Each of the four roles below independently evaluates the decision, working only from the shared evidence and its own criteria. Do not let one role's reasoning leak into another's, each should read as if it were the only one in the room.

For each role, produce:
- **Verdict**: support / oppose / conditional support
- **Reasoning**: 2-4 sentences, tied directly to specific evidence, not general principle
- **Top risk**: the single biggest concern from that role's specific vantage point

**CEO lens, strategy and return.** Does this fit the long-term direction and competitive position, is the likely return worth the risk being taken at a company level, is the timing right. This role does not care about how it gets executed, only whether it should be done at all.

**COO lens, execution and operations.** Can this actually be delivered with current people, systems, and processes, what breaks first under the current setup, is the timeline realistic given operational reality. This role does not care about long-term strategy, only whether the organization can actually pull it off.

**PM lens, scope and delivery risk.** What is the real scope once dependencies are accounted for, where are the points most likely to slip or cause rework, what's needed from stakeholders to keep this on track. This role does not care about whether the idea is strategically sound, only about what it takes to actually ship it.

**Founder lens, speed and validation.** What is the cheapest and fastest way to test this before committing fully, what is the cost of moving slowly on this compared to competitors or the market, is there a smaller version worth trying first. This role does not care about polish or process, only about speed to a real answer.

The four roles above run every time. Add the following on top when the decision calls for them, each one answers a narrow question the core four don't cover, and each one needs specific internal evidence from the user to say anything grounded, gathered in Step 2:

**CFO lens, numbers.** Add when the decision involves real cash outlay, margin impact, or financing. What does this do to cash flow, margin, and unit economics, what has to be true financially for this to pay off, what's the downside case in rand or dollar terms. Needs current revenue and cost figures.

**HR lens, people.** Add when the decision touches staffing, scheduling, overtime, hiring, or has a labour-compliance angle. Does this put unreasonable strain on current staff, is it compliant with the relevant labour rules, what does it do to morale and retention. This role doesn't care about strategy or scope, only the people actually carrying it out. Needs current headcount and overtime or pay rates.

**Marketing lens, demand.** Add when the decision is customer-facing and depends on people finding out about it, a price change, new hours, a new product, a campaign. Does anyone outside the business actually know this is happening, what does it cost in time or money to tell them (social posts, signage, email, ads), does the message match how the business is positioned. This role doesn't care about operations, only whether demand actually shows up. Needs the current marketing budget and whether promotional material already exists or still needs to be made.

### Step 4: Cross-examine

This step does not add a new opinion. It stress-tests the four the panel already gave.

Read all four verdicts against the evidence pack and:
- Identify where roles contradict each other (for example, the CEO likes it strategically but the COO says it can't be executed as scoped)
- For each contradiction, check which side is actually backed by the evidence pack versus which side is just asserted with confidence
- Ask, for each verdict, what would have to be true for it to be wrong
- Flag any verdict that isn't actually supported by anything in the evidence pack, confident wording is not evidence

The output of this step is not a fifth opinion, it's an assessment of which concerns are load-bearing and which are noise.

### Step 5: Final call

Produce one recommendation, not a summary of four opinions. Use the output template below exactly.

## Output template

```
**Quick answer:** [Yes / No / Conditional] — [one-sentence reason] — Confidence [X/5]

## The Decision
[One or two sentences restating what's being decided]

## Active Lenses
[The core four, plus whichever of CFO / HR / Marketing joined, and one clause on why]

## Evidence Snapshot
**From you:**
- [Fact you provided]
- [Anything asked for but not available, named as a gap]

**From research:**
- [Fact, with source]
- [Any research gaps, named honestly]

## Panel Verdicts

**CEO (strategy):** [verdict] — [reasoning]
**COO (execution):** [verdict] — [reasoning]
**PM (delivery):** [verdict] — [reasoning]
**Founder (speed):** [verdict] — [reasoning]
[**CFO (numbers):** [verdict] — [reasoning], if used]
[**HR (people):** [verdict] — [reasoning], if used]
[**Marketing (demand):** [verdict] — [reasoning], if used]

## Cross-Examination
[Contradictions found, which side the evidence actually supports, weak verdicts flagged]

## Final Call
**Recommendation:** [clear yes / no / conditional, stated plainly]
**Confidence:** [X/5]
**Why:** [2-3 reasons, tied to evidence, not restated opinions]
**What would flip this:** [the specific fact or event that would change the call]
```

## Guardrails

**No named real people.** Don't frame a lens as "what Jeff Bezos would say" or attribute views to a specific living or historical individual. That produces a caricature, not insight, and risks putting invented words in a real person's mouth. If a well-documented, publicly sourced principle is genuinely relevant (for example, a point from a company's published shareholder letters or a widely cited operating framework), it's fine to cite it as a source, but the lens itself stays role-based, not person-based.

**The confidence score is not a statistic.** It's a compressed summary of how well the evidence supports the call. Never give a score without the reasons attached next to it.

**Evidence gaps get named, not filled.** If the research step can't find something a role would need, or the user doesn't have a number on hand, say so in the Evidence Snapshot instead of letting a role reason as if the fact were known.

**Ask for what's needed, nothing more.** Internal data requests go only to the roles actually active for this decision, batched into one short, specific set of questions, not a generic intake form covering every role that could theoretically exist. If an answer isn't available, proceed with it named as a gap rather than stalling.

**Don't let this replace judgment.** This produces a structured, evidence-grounded starting point for a decision, not a verdict to be followed blindly. Say so if the user seems to be treating the output as more certain than it is.

## Extending this

To add a role beyond the four core lenses and the three conditional ones built in (legal, supply chain, whatever the business needs), give it the same treatment: a name, a one-line description of what it does and doesn't care about, a narrow question it answers, and a note on what internal evidence it needs from the user. A role without a narrow question will drift into generic commentary and stop pulling its weight.
