---
title: "Downgrades, Swaps, and the Classification You Never Built"
date: 2026-10-30
url: https://revopsinflection.substack.com/p/downgrades-swaps-and-the-classification
---

A RevOps leader on HubSpot joined a weekly call late last month because a brainstorm on one question had made them lose track of time: where does a downgrade go?

The team logs downgrades as a separate closed-lost deal type so they stay out of bookings. A mid-contract product swap ends up split across multiple records. And the only way a mid-contract downgrade actually reaches ARR is through the renewal deal months down the line. It was the 2nd version of this conversation in one week.

Thanks for reading RevOps Unfiltered! Subscribe for free to receive new posts and support my work.

## The workaround everyone builds

When a customer wants to drop seats, downgrade a tier, or swap products mid-contract, most systems break. To keep sales commissions clean and prevent negative numbers from distorting current-period bookings, RevOps teams invent workarounds. They route downgrades into a custom "Closed-Lost" deal type or park them in pipeline limbo until the contract expires.

The mechanics are understandable, but the side effects are severe:

  * Downgrades get logged as closed-lost deals to isolate them from sales rep performance.

  * Product swaps require multiple records to track the off-boarding of SKU A and the onboarding of SKU B.

  * The negative ARR impact is effectively hidden from active retention metrics, only hitting the ARR bridge when the formal renewal deal finally generates.




This isn't just an operational preference; it is often driven by hard platform constraints. For instance, HubSpot's line item API explicitly states that "The `price` specified within the `properties` field cannot be negative" ([HubSpot developer docs](https://developers.hubspot.com/docs/api-reference/crm-line-items-v3/guide)). When the system literally forbids a negative price on a line item, admins are forced to hack the architecture.

By contrast, enterprise CPQ engines handle this natively. Salesforce CPQ asks you to "always enter the total 'end result' quantity" on an amendment and calculates a reduction "as a credit," displaying the Net Total as a negative value ([Trailhead](https://trailhead.salesforce.com/content/learn/modules/contract-amendments-with-salesforce-cpq/change-an-existing-contract)). That is Snapshot and Delta logic hardcoded into a quoting engine. But for companies without enterprise CPQ, RevOps has to build that logic by hand.

## Picklist NRR

Most SaaS companies report Net Retention Rate (NRR) and Gross Retention Rate (GRR) using **Picklist NRR** \- retention numbers assembled entirely from manual dropdown labels on the Opp/Deal Type (`Expansion`, `Renewal`, `Upgrade`) chosen by a rep.

Relying on rep picklists to measure ARR movement creates blind spots across the board:

  * **The Net-Zero Mask:** A renewal deal that includes a $20k price increase and a $20k seat reduction nets out to $0. The rep tags it "Flat Renewal," completely hiding both a price expansion and a product downsell.

  * **The False Upsell:** A rep selects "Expansion" on a contract modification simply because a new product SKU was added, even though the net ARR delta on the account was negative.

  * **Parent/Child Mismatches:** A child account completely churns, but because the parent account renewed at a slightly higher spend, the deal rolls up as a parent-level renewal, sweeping gross churn under the rug.




## Snapshot, Delta, Label

To fix Picklist NRR, you have to disconnect the classification of a deal from human selection and let system logic handle the math.

### Snapshot

At the exact moment a transaction initiates, record the account's baseline ARR, active SKU-level entitlements, contract terms, and parent-child hierarchy position as they stood before the deal.

  * **Why it matters:** You can't measure change if you don't have an immutable record of where you started.

  * **How to tell if you have it:** Pick five accounts expanded last quarter and try to programmatically reproduce each account's SKU-level ARR as of 24 hours prior to close. If you can't do it without opening old PDFs or running manual billing queries, you don't have a snapshot.




### Delta

Calculate the line-by-line net variance between the baseline Snapshot and the new state across price, volume, and SKU changes.

  * **Executing Swaps:** To model a product swap cleanly at the line-item level, one path would be to create a zero-price line item carrying the historical ARR of the sunset SKU alongside a new line item for the replacement SKU, preserving the true net ARR delta at the deal level.

  * **Isolating Drivers:** Separate pure price increases from seat growth and new product cross-sells.

  * **How to tell if you have it:** Try to split last year's expansion ARR into price increases, seat growth, and new product adoption. If that calculation requires spreadsheet gymnastics, your delta logic lives only at the deal summary level, not line-item level.




### Label

Apply a system-calculated formula field that evaluates the net ARR delta and automatically assigns the deal classification (`New Logo`, `Expansion`, `Flat Renewal`, `Downsell`, or `Full Churn`).

  * **Governance:** Reps record operational facts: units, products, and prices. The system assigns the label based on math.

  * **Parent vs. Child Rules:** Establish explicit system rules for how churn at a child account impacts parent-level reporting.

  * **How to tell if you have it:** Audit last quarter's closed deals and count every record where the rep-assigned deal type disagrees with the mathematical sign ($+$ or $-$) of the deal's ARR delta.




## The thread to the renewal

Every mid-term transaction - whether an upsell, product swap, or partial downsell -must update the active account state and link directly back to the master renewal record.

When mid-contract amendments exist as isolated deal records without feeding the active entitlement state, the upcoming renewal deal generates off outdated contract terms. Account managers enter renewal conversations quoting against the wrong baseline, leading to billing disputes, delayed closes, and unrecorded churn.

  * **How to tell if you have it:** Take ten renewals due next quarter and compare their starting line items against active product entitlements in your billing system.




### Callout: PE / Executive Reality Check

During private equity acquisition diligence or Quality of Earnings (QoE) audits, buy-side analysts throw out CRM picklists. They rebuild NRR and GRR bridges line-by-line directly from raw billing schedules and contract records. If you've been in SaaS for any amount of time, you've seen the snowball/ARR bridge.

When mid-contract downgrades parked in "Closed-Lost" deals or sweeps surface during diligence, reported retention numbers collapse. It is common to see a company claiming a healthy 105% NRR get re-rated down to 94% NRR once downgrades are correctly matched to their actual timing. That adjustment directly lowers entry ARR and can hit the valuation multiple by 1-2x during final negotiations.

## Diagnostic: run these on your own data

Before putting NRR numbers in front of your board or an investor, run these four data pulls:

  1. **The Hidden Downgrade Audit:** Pull every Closed-Lost deal categorized as a "Downgrade" or "Swap" over the last four quarters. Verify whether its negative ARR impact was recognized in the quarter it occurred or deferred until renewal.

  2. **The Disagreement Index:** Compare the rep-assigned deal type picklist against the mathematical sign of `(Ending ARR - Prior ARR)`. Count total discrepancies.

  3. **The Expansion Decomposition:** Break down last year's total expansion ARR into pure price increases, seat/volume additions, and new product cross-sells.

  4. **The Renewal Alignment Check:** Take next quarter's top 20 renewal opportunities and verify that starting line items match current active entitlements.




## The move

Determine how sophisticated you want this to be. You could deploy two standard system fields at the deal level: `Prior ARR` and `Ending ARR`. Build an automated formula field (`System Calculated Deal Type`) directly alongside your existing rep-facing picklist. You could build a custom object to hang off the Opp/Deal to capture all of the information (we've done this). You could also use the warehouse to handle these complex calculations to build a simple to use data mart.

Whichever path you take, run everything through the end of Q4, quantify the discrepancy count, and bring the hard variance metrics to your January board prep.

Let reps record what changed, and let the system decide what to call it.

Thanks for reading RevOps Unfiltered! Subscribe for free to receive new posts and support my work.