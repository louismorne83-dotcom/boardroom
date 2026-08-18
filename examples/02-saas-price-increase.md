# Example: finance-heavy decision

**Prompt:** Should our SaaS company raise subscription prices by 10% next quarter to offset rising cloud costs?

**Placeholders supplied when asked:** ~R450,000 MRR, 78% gross margin, cloud costs up roughly R35,000/month, current monthly churn ~2% (about 22% annualized), plan is 10% applied to everyone at once, no grandfathering.

---

**Active lenses:** the core four, plus CFO (real margin and cash impact). Not HR, no staffing angle. Not Marketing, judgment call, existing customers see this as a billing change rather than something needing awareness material.

**Quick answer:** Conditional yes, not as originally scoped. Confidence 3/5.

## Evidence Snapshot

**From you:**
- MRR ~R450,000, gross margin ~78%
- Cloud costs up ~R35,000/month
- Current monthly churn ~2% (~22% annualized)
- Plan: 10% on all tiers, new and existing, no grandfathering

**From research:**
- Industry churn benchmarks: scale-stage SaaS ($8M+ ARR) targets 3-5% annual churn, early-stage (<$1M ARR) treats ~8% annual as acceptable. At ~22% annualized, this company's churn already sits well above both benchmarks, before any price change.
- Gap: no reliable, sourced figure found for how much a 10% increase specifically moves churn, that's company-specific and needs direct testing.

## Panel Verdicts

**CEO (strategy):** Conditional, flags the churn number. Passing through a real cost increase is reasonable, but a company already churning well above benchmark isn't well positioned to absorb more attrition from an unpopular change.

**COO (execution):** Supports operationally, flags a support-ticket spike is coming after the change goes live.

**PM (delivery):** Opposes the "everyone at once" version specifically. Recommends grandfathering existing customers and applying the increase to new signups first.

**Founder (speed):** Supports testing the number on a smaller cohort before locking in 10%.

**CFO (numbers):** Conditional, with the math laid out. Cloud costs are about 7.8% of MRR. A clean 10% increase, if it held with no churn, would add roughly R45,000/month, comfortably covering the cost increase. But at the current elevated churn rate, even a modest bump from a badly rolled out increase could erase that gain.

## Cross-Examination

The CFO's math and PM's grandfathering plan connect directly: the blanket version is the one most exposed to the CFO's downside case, since there's no way to see the churn reaction before it hits the whole customer base. The CEO's "this is reasonable" verdict only actually holds under the phased version, not the blanket one originally proposed, a real contradiction the evidence resolves rather than a stylistic preference.

## Final Call

**Recommendation:** Conditional yes, not as originally scoped. Apply the 10% to new signups first, grandfather existing customers for a stated window, and treat new-signup conversion and existing-customer churn over that window as the real test of the number.

**Confidence:** 3/5. The cost math supports repricing, but the already-elevated churn rate and the absence of company-specific price-elasticity data cap confidence in the blanket version.

**Why:** cloud costs genuinely justify a price move and the CFO math shows real headroom if churn stays flat, but current churn is already roughly double the healthy SaaS benchmark, leaving less room to absorb a churn spike from a badly rolled out increase.

**What would flip this:** if new-signup churn holds steady or improves over the grandfather window, roll the increase out to the full base. If it worsens, the number needs revisiting before the rollout continues.
