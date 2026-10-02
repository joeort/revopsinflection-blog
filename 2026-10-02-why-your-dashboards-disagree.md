---
title: "Why Your Dashboards Disagree"
date: 2026-10-02
url: https://revopsinflection.substack.com/p/why-your-dashboards-disagree
---

Last week a CRO called a 15-minute meeting for one reason: three reports were showing three different upsell and expansion numbers.

Nobody had a bad dashboard. Three smart people had each built a reasonable one. They still could not agree on what the company had sold.

Thanks for reading RevOps Unfiltered! Subscribe for free to receive new posts and support my work.

That is the board-meeting version of this problem. You walk in with a number, someone has a different number, and the next 20 minutes go to arguing about whose is right instead of what to do about it.

We found three causes in that one call. Each one generalizes.

## **Cause 1: The filter**

The CRO's report filtered on a quota attainment field that only populates when an AE is attached. Any opportunity without an AE dropped out, so totals were understated.

Removing the filter pulled in everything, but it also pulled in renewals with churn and downsells. To get an actual growth number, the report needed an extra filter: ARR delta greater than zero.

Same data. A hidden filter and a missing filter, two different answers.

## **Cause 2: The date**

One group reported by close date. Another reported by renewal start date.

For a mid-contract upsell, the two dates are the same day. For a deal closed at renewal, they are not. A deal can close in Q3 and start in Q4, so it lands in Q3 in one report and Q4 in the other.

I said it plainly on the call: if you use two different dates, you will get a disconnect any time you compare by period. Both dates are defensible. Define your metrics to this level of granularity. 

This is why you can't just assume AI will give you the right answer if you can't even agree internally. The mistake is not picking a date. The mistake is picking two without writing down which metric uses which.

## **Cause 3: The field**

The uplift report ran off an uplift percentage on the opportunity. That field defaults to 10%, and AEs often do not change it. 

The result: the report showed roughly 30K of uplift. The team agreed the real number for the quarter was closer to 100K. 

A formula can be perfect and still produce garbage if the field feeding it is a default nobody overwrote or audited. 

## **When the record and the report disagree**

A second scenario from a different cleanup effort.

We were fixing gaps in marketing lifecycle (LC) reconciliation. The CRM showed every opportunity flagged from August and found each one had an LC record, with the SQL date populated. 

My dashboard still showed 7 LC records with no opportunity link. Separately, about 22 opportunities had no LC record at all. There were multiple issues that caused issues in this scenario:

  * Order of import from a large conference

  * Incorrectly tagging a Campaign

  * Data syncs error-ing out




If you rely on AI to provide your results, would you get the right answer? Would you know how to validate? Would you even know there were discrepancies?

Which layer was lying: the record, the sync, or the report? You cannot answer that until you know where to look. 

## **The pattern: four layers**

When two numbers disagree, the cause sits in one of at least four places. 

\- **Definition:** what does the metric mean, and which date anchors it?

\- **Filter:** what does each report include and exclude, and is any of that hidden?

\- **Field:** is the input populated by a human, a default, or a system, and how often is it wrong?

\- **Refresh:** does the BI layer match the CRM right now, and who checks? What is the refresh sequence?

Most teams jump straight to rebuilding the dashboard. That fixes the Filter layer at best. The other three layers stay broken and the numbers drift apart again within a quarter.

## **The move**

Take the one metric your board sees most often. List every report that shows it. Run all of them for the same period and compare.

PS: I ran the BI team for a unicorn data catalogue provider and the data lineage and report certification processes were rigorous for a reason. SMBs don't need that level of complexity (our Emerging segment was from $1B-10B) but that doesn't mean you shouldn't approach your reporting in the same way.

For every gap, name the layer. Then write the definition in one place and give it one owner. 

If you cannot name who owns the definition of expansion ARR, you do not have an expansion number. You have a few opinions with charts attached.

It's RevOps job to deal in the detail.

Thanks for reading RevOps Unfiltered! Subscribe for free to receive new posts and support my work.