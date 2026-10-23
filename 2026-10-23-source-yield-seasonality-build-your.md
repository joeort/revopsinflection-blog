---
title: "Source, Yield, Seasonality: Build Your 2027 Pipeline Model From Bookings Back"
date: 2026-10-23
url: https://revopsinflection.substack.com/p/source-yield-seasonality-build-your
---

During a 2027 planning session this month, a leadership team cut their historical win rates by pipeline source. Outbound BDR-sourced deals came back with a weak win rate and the smallest deal sizes, and events came out as the strongest source. The 2027 model on the table still calculated the pipeline requirement as BDR headcount multiplied by an assumed number of meetings per head.

I told them on the call that this approach all needs to go away. A pipeline model built from the hiring plan can only hand the hiring plan back to you, so it never tests whether those hires can deliver the number.

Thanks for reading RevOps Unfiltered! Subscribe for free to receive new posts and support my work.

## The Model That Grades Its Own Homework

I call this the Headcount Echo: pipeline calculated as planned reps multiplied by a production assumption per head. Whatever hiring plan goes in comes back out as the pipeline forecast, and the model grades its own homework without ever looking at what the market is actually yielding.

I've built this version myself as a bottoms-up version. The pipeline model I published in January built the BDR line from a headcount census, ramp, and meeting quotas, and it has the same flaw as described here when used in a vacuum. When every BDR inherits the same production assumption, the model can't tell you which source is earning its keep. An outbound pipeline dollar gets treated as equal to an inbound or event dollar.

The damage shows up once execution starts. When a source's yield is weak, adding heads to it raises spend faster than it raises bookings, and nothing in the model would have warned you.

## What the Source Cut Showed

Slicing closed opportunities by pipeline source is usually enough to reshape the plan, even when the data is only directional. In this case the ranking was clear before anyone argued about attribution.

> "Fuzzy math over time shows trends." \- great quote by a CMO Advisor, 15 years ago

In the companies I've worked with, the ranking tends to land close to this:

  * **Events and executive programs:** high win rates and large deals, as long as post-event routing and follow-up are tight.

  * **Partner / channel:** strong win rates and larger deals because trust carries over from the partner, with volume capped by how mature the ecosystem is.

  * **AE self-sourced:** high win rates on targeted accounts, capped by rep selling time. This is typically skewed up by reps only putting deals in that are of higher quality.

  * **Inbound:** high volume and predictable velocity, with moderate win rates and deal sizes.

  * **Outbound / BDR:** the lowest win rates and smallest deals, so it needs the most opportunity volume per booked dollar.




Your ranking will differ, which is why you run the cut on your own data. The data caveats are where most teams stall: a short history of clean pipeline-entry tracking, inbound deals tagged as BDR-sourced because a rep touched them first, RFP deals crediting the AE as originator by default, and small deal counts on some sources.

Rank your sources on the directional data now and fix attribution in parallel. If you wait for clean attribution, you'll plan another fiscal year on the Headcount Echo.

## Source, Yield, Seasonality

Top-down coverage multipliers ("we need 4x across the board") skip the channel math entirely. A bottom-up source model starts with the bookings each source has to carry, applies that source's historical yield, and spreads the required pipeline creation across the calendar. Headcount is the last step.
    
    
      [ Bookings Target by Source ]
                    │
                    ▼
      [ ÷ Historical Yield (Win Rate, Deal Size) ]
                    │
                    ▼
      [ = Pipeline Needed by Source ]
                    │
                    ▼
      [ Spread Across the Calendar ]
                    │
                    ▼
      [ ÷ Output per Ramped Head = Headcount ]
    

### 1\. Source

Set the share of 2027 bookings each source is expected to carry before anyone discusses headcount or budget. Bookings are the commitment you make to the board, and pipeline is the work in progress required to deliver them, so the allocation starts with bookings.

> "Begin with the end in mind." \- Stephen Covey, 7 Habits of Highly Effective People

Illustrative example: on a $10M net-new bookings plan, events carry 50% ($5.0M) and outbound BDR carries 15% ($1.5M). Inbound, partner, and AE self-sourced carry the remaining 35%.

**How to tell if you 're in this trap:** your model has a pipeline target for each source and one unallocated bookings number. That means the shares were set by habit and in a silo; disconnected from the overall plan.

### 2\. Yield

Apply each source's own win rate and deal size. A blended average across the business hides exactly the differences this model exists to expose.

Carrying forward the same $10M plan:

  * **Events:** $5.0M at a 30% win rate needs $16.7M of created pipeline. At a $60K average deal, that's 83 wins and 278 qualified opportunities.

  * **Outbound:** $1.5M at a 10% win rate needs $15.0M of created pipeline. At a $25K average deal, that's 60 wins and 600 qualified opportunities.




Outbound needs nearly as much pipeline as events to book less than a third of what events book, and it needs more than twice the opportunity count. The operational burden shows up in opportunity counts well before it shows up in the financials, and 600 opportunities call for a very different SDR and AE capacity plan than 278.

Watch for the **blanket uplift** : a standard 10% improvement applied to every line in the spreadsheet because "we'll get incrementally better at everything." An uplift belongs on a source only when something documented changes there, such as moving outbound to signal-based account targeting or adding stage-gate criteria in the CRM. Also beware of incremental improvements piling on top of each other. 5% here, 10% there, another 5% here and you've got >20% increases without evidence to back it up.

**How to tell if you 're in this trap:** count the lines in your model with an assumed conversion uplift, then count the ones with a written operational plan behind them. Remove every uplift that doesn't have one.

### 3\. Seasonality

The calendar decides when a source can produce. Events happen on specific dates, program spend moves by quarter, and new reps need ramp time before they reach full productivity. Ask for next year's event calendar before you model event pipeline, even if it's rough.

Build in the lag. Illustrative: an event in February creates qualified pipeline in March, and on a six-month sales cycle that pipeline books in Q3. Run the same math backward and most of the event pipeline behind your Q1 2027 bookings came from events held in the second half of 2026.

**How to tell if you 're in this trap:** monthly pipeline creation for each source is a flat line across twelve months, which means the calendar never made it into the model.

## Where Headcount Comes Back In

Once you have required pipeline by source and by month, divide it by what one fully ramped head in that source realistically produces. That gives you heads by source and by hire date, and every head traces back to a bookings requirement you can defend to the CEO or the board.

Outbound has a ceiling. Its output is bounded by the size of the addressable market and how often you can credibly touch an account, so past that point additional heads add cost faster than they add pipeline. Check that ceiling before approving the next BDR req, and make sure every source's share has a named owner and a written execution standard next to the percentage.

> **PE / Executive Reality Check:** A hiring plan justified by a pipeline target that was calculated from the hiring plan is circular. In diligence and operating reviews, expect sponsors to ask for yield by source. If your model can't answer that question, they will treat the growth plan as unvalidated risk.

## Diagnostic: Run These Pulls on Your Own Data

Before signing off on next year's numbers, run these five pulls in your CRM:

  1. **Source yield:** export every opportunity that closed, won or lost, in the last 12 months. Calculate win rate by count and by dollars, plus average and median deal size, by pipeline source, and rank the sources. A big gap between average and median means a few large deals are carrying that source. This is a commonly skipped step that may cause issues when your volumes hit but deal sizes shrink due to lower high ticket price deals.

  2. **Allocation check:** put that ranking next to where GTM headcount and program dollars sit today. A major mismatch means you're planning on the Headcount Echo.

  3. **Attribution audit:** sample recent wins in each source and check the label. Look for inbound leads credited to the BDR who followed up, event deals credited to outbound, and RFPs crediting the AE by default.

  4. **Uplift scrub:** every conversion improvement in the model gets a written operational reason or resets to historical performance.

  5. **Calendar overlay:** plot required monthly pipeline creation by source against the event calendar, program spend, and hiring plan.




## The Move

This week, open the planning workbook and rebuild one tab: net-new bookings by source, divided by historical yield, spread across the calendar, with headcount calculated last. Bring it to the next planning meeting alongside the headcount-driven version and let the gap between the two numbers start the conversation.

Plan the bookings by source first, and the headcount answer falls out of the math.

* * *

We love planning exercises. Reach out if you need support in your planning. We have capacity opening up in November for the first time in a while!

Thanks for reading RevOps Unfiltered! Subscribe for free to receive new posts and support my work.