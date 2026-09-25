---
title: "Can Any Company Stand Up a Data Warehouse?"
date: 2026-09-25
url: https://revopsinflection.substack.com/p/can-any-company-stand-up-a-data-warehouse
---

The mid-market CEO and CRO's dilemma: you want the analytical rigor of a company three times your size, but you can't justify a data engineer, an analytics engineer, and a BI hire on a sub-$50M ARR budget. So you do nothing, and every metric is a moving target or a discussion of what the right number is.

That's the wrong tradeoff. A Data Office shouldn't prevent you from gaining the benefits of quality data. In the end, it's 4 functions, done in order, on a defined architecture. You can get started with much of the benefits with some simple tooling, SQL that Claude can write for you/r data analyst and your internal metric definitions and you're set up!

Thanks for reading RevOps Unfiltered! Subscribe for free to receive new posts and support my work.

## What a data office actually does

Strip the title away and a Data Office produces four things:

  1. **One system of record for the numbers** , not five spreadsheets that disagree. 

  2. **One definition per metric** , written once, referenced everywhere.

  3. **A history no source system keeps** , so you can answer "what did pipeline look like 90 days ago?"

  4. **Governed access** , so BI tools and AI agents pull from the same governed layer instead of each inventing their own SQL (no more arguing over who has the right number).




None of that requires a team. It requires an architecture that separates where data lands from where it gets defined from where it gets consumed.

## The architecture, in five layers

**Source systems stay dumb.** CRM, conversational intelligence (Gong, Chorus, Clari), email engagement, calling/sequencing, product usage, third-party intent. Each one is a capture tool. None of them is asked to be the analytical truth despite what we've been trying to force Salesforce into.

**A warehouse becomes the real system of record.** Snowflake or BigQuery, landing every source untouched. This is the load-bearing mental shift: the CRM stops being where the numbers live and becomes one input among six. A great note I saw on LinkedIn not too long ago talked about how CRMs are always a Source for data tools, not a Destination.

**dbt transforms once, not five times.** Staging cleans and dedupes. Marts encode business logic (deal-age buckets, stage definitions, scoring) exactly once, in one place, so a rep, a dashboard, and an AI agent are never computing **Pipeline coverage** three different ways. Curated marts: Bookings, Pipeline, Customer 360, Product.

**A semantic layer is the actual product.** This is the piece most companies skip, and it's the piece that makes everything downstream trustworthy. One definition of every metric, exposed identically to a BI tool and to an AI agent. Without it, an LLM given warehouse access will happily compute win rate a different way than your dashboard does, and nobody will notice until a board meeting.

**(Optionally) Reverse ETL closes the loop.** Enriched fields (scores, signals, health) sync back into the CRM, so the rep working the account benefits from the same layer the executive dashboard reads from. Coalesced signals get written to the CRM and a slack message to the rep.

## Why this is affordable now in a way it wasn't three years ago

The stack underneath all five layers is largely open source and near-free at this scale: dlt for ingestion, dbt Core for transformation, a warehouse with a real free tier, GitHub Actions for orchestration. Infrastructure was never the expensive part of a data function. Headcount was, because someone had to hand-write every pipeline, every model, every semantic definition.

AI collapses that labor cost. A well-scoped starter template plus an LLM that can write and debug dbt models means the build no longer requires a data engineering team, it requires someone who can follow a known-good pattern and adapt it. That's a fundamentally different hire, or no hire at all, if you bring in a fractional partner to stand it up.

Even setting yourself up to be Enterprise Ready can include big names at low cost:

  * Data warehouse options

    * **BigQuery** is effectively free for most smaller businesses already on Google Workspace. 

    * **Supabase** has a strong free tier and can scale up pretty quickly.

    * **Snowflake** is synonymous with Enterprise but with the right structure and refresh/compute schedules, you can get a decent handle on your business for less than you think.

  * Extraction options

    * Fivetran is expensive but a known commodity and easy to set up

    * Airbyte has an open source option that means no licensing cost but you do have the compute costs. The Cloud version is a lighter lift but not quite as easy as Fivetran.

  * Visualization options

    * Metabase has limited visualization options but it could be a good place to start

    * Lightdash requires dbt infrastructure but is relatively easy to get decently far on the platform

    * PowerBI for MSFT shops or Looker for Google shops may already have much of the cost paid for or the licensing costs are pretty low

    * Claude artifacts or github pages built on top of the warehouse




[![](https://substackcdn.com/image/fetch/$s_!fVDM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c6500e8-94a4-4286-8a88-43aa87cddc36_1200x1650.png)](https://substackcdn.com/image/fetch/$s_!fVDM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c6500e8-94a4-4286-8a88-43aa87cddc36_1200x1650.png)

## The semantic layer is why "AI-ready" isn't a checkbox

Every vendor is pitching "AI-ready data" right now. Everyone's trying to get you onto their agent. The semantic layer is the actual mechanism: it's what lets a home-grown AI agent answer "which reps have high talk-time but low pipeline coverage" correctly, because talk-time and coverage are defined once, upstream, instead of guessed at by the model in real time. 

Buy the infrastructure. Build the intelligence. - [The Signal](https://www.thesignal.club/p/xbow)

Skip this layer and you haven't completed your AI readiness. Want to move faster? Get this right.

## Who this is actually for

This isn't for every company. 

If you're running a single CRM with under ten users without any additional sales tools, you don't need this, you need a better report. This is for the company with multiple source systems that has to be joined to answer a real question, a genuine need for trend history the CRM can't natively provide, and someone on the executive team who will actually act on what the layer produces. Usually that's triggered by a new CRO or CFO, a post-raise mandate, or a missed quarter that exposed how little anyone trusted the existing numbers. Sometimes it's just a curious executive that wishes they could get answers that they can't.

## The bottom line

The CRM tells you what a rep entered. The warehouse tells you what actually happened. Building the second one used to require a department. Now it requires an architecture, a fixed-scope build, and a maintenance retainer, not a req.

Reach out to us if you want to talk about your specific situation and let's find the best path for you.

Thanks for reading RevOps Unfiltered! Subscribe for free to receive new posts and support my work.