# Which US Airline Is Most Likely to Make You Late?
## Your Mission: Build an Airline Delay Scorecard

---

## The Scenario

**You're a data analyst at TravelSmart**, a student-focused travel recommendation platform helping UVA students book flights home for breaks and summer vacations. Your platform has been gaining popularity among college students looking for affordable, reliable flight options—but lately, the customer support team has been flooded with complaints.

*"I missed my connecting flight because of a 2-hour delay!"*  
*"My airline cancelled my flight home for Thanksgiving with only 4 hours notice."*  
*"I've been late to three family events this year because of delays."*

The TravelSmart team realizes they need to do better. Right now, the platform recommends flights based purely on price. But **what if you could also factor in reliability?** What if students could see which airlines are most likely to get them home on time?

Your manager pulls you into a meeting: **"We need an airline scorecard. Which carriers should we be recommending to minimize delay risk? I need data-driven insights—not guesses. Can you figure this out?"**

**This is your chance to make a real impact.** Millions of students fly home each year, and your analysis could help them avoid the frustration of delays and cancellations.

---

---

## The Challenge

You have access to **real flight performance data from 2022-2024**, collected and published by the U.S. Bureau of Transportation Statistics (BTS)—the same data that government agencies and news outlets use to rank airlines. This isn't toy data or a simplified sample. This is the real deal: **over 18 million flight records** from 9 major U.S. carriers, including every departure time, arrival time, delay, and cancellation.

Your task is to transform this massive dataset into actionable insights. Specifically, you need to:

### 1. Define "Late" Using Industry Standards
The BTS uses a clear definition: **a flight is considered delayed if it arrives 15 or more minutes after its scheduled arrival time.** This is the gold standard that airlines, regulators, and consumer advocates all use. Your analysis must apply this same threshold to ensure your findings are comparable to official rankings.

### 2. Compute Airline-Level Delay Rates
For each of the 9 airlines in your dataset, calculate:
- **Delay rate:** What percentage of flights arrive ≥15 minutes late?
- **Cancellation rate:** What percentage of flights are cancelled outright?
- **Average delay magnitude:** When flights are delayed, how late are they on average?

These metrics will form the backbone of your airline scorecard.

### 3. Build Visual Comparisons
Numbers alone won't convince stakeholders. You need to create **clear, professional visualizations** that show:
- Which airlines have the highest delay rates (worst performers)
- Which airlines are most reliable (best performers)
- Whether delay risk and cancellation risk go hand-in-hand

Think: bar charts ranking airlines, scatter plots comparing metrics, and clean tables summarizing findings.

### 4. Validate Against Official Rankings
The BTS publishes annual airline rankings based on on-time performance. Your analysis should produce similar results—but you'll be working with raw flight-level data, not pre-aggregated summaries. **Compare your computed rankings to the official BTS tables.** Do they match? If not, why? (Hint: differences might arise from sample restrictions, time windows, or route mix.)

### 5. Deliver a Data-Driven Recommendation
Finally, synthesize everything into a **clear, evidence-based report** that answers the core question: **Which airline should TravelSmart recommend to students who want to minimize delay risk?** Your recommendation should be backed by data, acknowledge limitations, and provide actionable insights.

---

---

## What You'll Discover

By the end of this case study, you'll have concrete answers to questions that affect millions of travelers:

### The Core Question
**Which major U.S. airline has the highest chance of making you late?**

Is it a budget carrier trying to maximize aircraft utilization? A legacy airline with complex hub-and-spoke operations? Or perhaps a regional player facing weather challenges in certain markets?

### The Magnitude of Differences
**How much do delay rates actually vary between airlines?** Are we talking about marginal differences (18% vs. 20%), or are some airlines dramatically worse than others (15% vs. 30%)? Understanding the spread helps you assess whether airline choice really matters for travelers.

### The Reliability Trade-Offs
**Do airlines with high delay rates also have high cancellation rates?** Or are these independent problems? Some airlines might keep flights running (avoiding cancellations) but accept more delays, while others might proactively cancel to protect on-time performance. Your scatter plots will reveal these trade-offs.

### Validation and Credibility
**How do your findings compare to what government agencies report?** The Department of Transportation publishes annual rankings of airline on-time performance. If your analysis produces similar results, it validates your methodology. If there are differences, you'll need to explain why—and that's where the real learning happens.

### Real-World Context
Every year, the DOT ranks airlines on these exact metrics. News outlets like USA Today, Bloomberg, and regional newspapers publish "best and worst airlines" lists based on this data. **Now you'll do the ranking yourself**, using the same raw data they use. This isn't a classroom exercise disconnected from reality—this is the actual process that informs consumer decisions and airline reputations.

---

## Your Deliverables

### 1. **Jupyter Notebook** (or R Markdown)
A reproducible analysis showing:
- Data exploration and cleaning steps
- Airline-level metric calculations (delay rate, cancellation rate, avg delay)
- Visualizations comparing airlines (bar charts, rankings)
- Interpretation of findings

### 2. **Written Report** (2-3 pages)
A professional summary answering:
- Which airline is most likely to make you late?
- How does your ranking compare to BTS official rankings?
- What might explain differences between airlines? (route mix, operational practices, etc.)
- What are the limitations of your analysis?

---

---

## Why This Matters

### Real-World Impact
**Over 700 million passengers fly domestically in the U.S. each year.** When airlines have high delay rates, it doesn't just inconvenience travelers—it costs them money (missed connections, hotel stays, lost productivity), damages airline reputations, and triggers regulatory scrutiny. Your analysis directly informs the same types of decisions that consumers, airlines, and policymakers make daily.

### Government Accountability
The **Department of Transportation** requires airlines to report delay data precisely so that poor performers can be identified and held accountable. Consumer protection laws, compensation policies, and even airline rankings in official reports all stem from this data. By working with BTS data, you're engaging with the same information used to regulate a multi-billion dollar industry.

### Practical Data Science Skills
This case study isn't about memorizing formulas—it's about **practical problem-solving with messy, real-world data**:
- **Handling large datasets:** 18 million rows won't fit in Excel
- **Domain knowledge application:** Understanding what "on-time" means in aviation
- **Aggregation and grouping:** Going from individual flights to airline-level insights
- **Validation:** Comparing your results to external benchmarks
- **Communication:** Presenting technical findings to non-technical stakeholders

These are the exact skills that employers value in data analysts.

### Portfolio-Worthy Project
When you're applying for internships or jobs, you need projects that demonstrate **end-to-end analytical thinking**:
1. ✅ You were given a real business question
2. ✅ You worked with authentic, large-scale data
3. ✅ You computed meaningful metrics and validated them
4. ✅ You created professional visualizations
5. ✅ You communicated findings clearly

**This case study checks all those boxes.** It's the kind of project you can confidently discuss in interviews: "I analyzed 18 million flight records to build an airline delay scorecard, validated my findings against government rankings, and identified which carriers have the worst on-time performance."

---

## Getting Started

### 📂 **Access the Repository**
All materials are in the GitHub repository:

**[https://github.com/davidmarip/CS3-DS4002](https://github.com/davidmarip/CS3-DS4002)**

### 📖 **Your Roadmap: How to Approach This Case Study**

#### **Phase 1: Context & Motivation (15-20 minutes)**
Before touching the data, understand how professionals approach this problem:
- **Read the USAFacts article** (`SUPPLEMENTAL_MATERIALS/USAFacts_Airline_Performance.pdf`): This is a blog-style piece written for the general public. Notice how they present airline rankings—what metrics do they emphasize? How do they visualize comparisons? This is your model for communication.
- **Skim the BTS documentation:** Understand the official definition of "on-time" (flights arriving within 15 minutes of schedule) and why that threshold matters.

**Goal:** Build intuition about what makes a good airline scorecard before you start coding.

#### **Phase 2: Data Exploration (30-45 minutes)**
Get familiar with your dataset:
- **Review the data dictionary** (`DATA/DATA_DICTIONARY.md`): What variables are available? What do they mean?
- **Load the data** and run basic checks: How many rows? How many airlines? What's the date range?
- **Spot-check individual records:** Pick a few random flights and manually verify that `ArrDelay15` makes sense given `ArrDelayMinutes`.
- **Check for missing data:** Are there nulls? Cancelled flights? How should you handle them?

**Key variable to understand:** `ArrDelay15` is a binary flag (0 or 1) that tells you whether each flight was delayed by ≥15 minutes. This is your primary outcome variable.

**Goal:** Understand the structure and quality of your data before attempting analysis.

#### **Phase 3: Metrics & Scorecard Construction (3-4 hours)**
This is the core analytical work:
- **Compute delay rate by airline:** For each carrier, calculate: `(number of flights with ArrDelay15=1) / (total flights) × 100%`
- **Compute cancellation rate:** What percentage of each airline's flights were cancelled?
- **Compute average delay magnitude:** For flights that were delayed, how late were they on average? (This shows severity, not just frequency.)
- **Create a comprehensive scorecard table:** Combine all metrics into one clean table showing all 9 airlines.
- **Build visualizations:**
  - Bar chart ranking airlines by delay rate (which is worst? which is best?)
  - Bar chart showing cancellation rates
  - Optional: Scatter plot of delay rate vs. cancellation rate to explore trade-offs

**Technical note:** Decide early whether to include cancelled flights in your delay rate calculation. Most analysts exclude them (a cancelled flight didn't "arrive late"—it didn't arrive at all). But document your choice.

**Goal:** Produce a clear, data-driven ranking of airlines by delay risk.

#### **Phase 4: Validation (30-45 minutes)**
Check your work against external benchmarks:
- **Open the BTS annual rankings** (`SUPPLEMENTAL_MATERIALS/BTS_Annual_Rankings_2022_2024.pdf`): These are the official government tables showing which airlines performed best/worst in 2022-2024.
- **Compare your ranking to theirs:** Are your top 3 worst airlines the same as BTS's? What about the best performers?
- **Discuss differences:** If your ranking diverges from BTS, why might that be? Possible reasons:
  - You may have used a sample of flights, not the full population
  - You may have filtered to domestic-only flights
  - Time aggregation differences (monthly vs. annual)
  - Route mix differences (BTS includes all routes; you might have fewer)

**Goal:** Demonstrate that your methodology produces credible results by validating against official sources.

#### **Phase 5: Communication (1-2 hours)**
Package your findings into a professional deliverable:
- **Write a 2-3 page report** with sections:
  - **Introduction:** What question are you answering and why does it matter?
  - **Methods:** How did you compute delay rates? What filters did you apply?
  - **Results:** Which airline is most likely to make you late? Show your scorecard and visualizations.
  - **Validation:** How do your findings compare to BTS official rankings?
  - **Limitations:** What factors does your analysis not account for? (e.g., route difficulty, weather patterns, hub congestion)
  - **Recommendation:** Based on your analysis, which airline(s) should TravelSmart recommend to students?

**Tone:** Write like you're presenting to your manager, not to a statistics professor. Be clear, confident, and evidence-based, but acknowledge what you don't know.

**Goal:** Deliver actionable insights in a format that non-technical stakeholders can understand and trust.

---

### ⏱️ **Time Budget Summary**
- **Phase 1 (Context):** 15-20 minutes
- **Phase 2 (Exploration):** 30-45 minutes
- **Phase 3 (Analysis):** 3-4 hours
- **Phase 4 (Validation):** 30-45 minutes
- **Phase 5 (Communication):** 1-2 hours

**Total estimated time:** 5-7 hours (spread over several days)

---

## Success Criteria

You'll meet expectations when you:

✅ Correctly apply the **BTS 15-minute delay standard**  
✅ Compute **at least 3 airline-level metrics** (delay rate, cancellation rate, avg delay)  
✅ Create **clear visualizations** comparing all 9 airlines  
✅ **Compare your results** to official BTS rankings and discuss differences  
✅ **Communicate findings** in a professional, evidence-based report  

See **`RUBRIC.pdf`** in the repository for detailed grading criteria.

---

---

## Tips for Success (Lessons from Past Students)

### Start with the Context
> **"The USAFacts article was super helpful—read it first to see how they present the data. It gave me a template for how to structure my own visualizations."** — Sarah M.

Don't skip the supplemental materials. They're not busywork—they show you how professionals communicate these findings to the public.

### Keep It Simple
> **"I almost overcomplicated this. The rubric says 'compute 3 metrics'—so I computed exactly 3 metrics and made them crystal clear. That's what mattered."** — James L.

Resist the urge to throw every possible statistic at the problem. A few well-chosen metrics, clearly explained and beautifully visualized, are far more valuable than a dozen half-baked calculations.

### Validation Is Your Friend
> **"My ranking was slightly different from BTS's official one. I panicked at first, but then I realized I'd filtered to domestic-only flights while BTS includes international. Once I explained that difference in my report, it actually showed I understood the data."** — Priya K.

Differences from official rankings aren't failures—they're opportunities to demonstrate critical thinking. Just explain why the differences exist.

### Document Everything
> **"I used a 10% sample of the data (2 million rows instead of 20 million) because my laptop was slow. I documented this in my notebook and report, explained why the sample was representative, and had zero issues with grading."** — Marcus T.

If you make practical adjustments (sampling, filtering, simplifications), just document them clearly. Transparency builds trust.

### Visualization Matters
> **"I spent an extra hour making my bar charts clean and professional. Added clear labels, sorted by delay rate, and highlighted the worst performer in red. My TA specifically called out my visualizations as a strength."** — Emily R.

Professional-looking charts signal that you care about communication, not just computation. Use axis labels, titles, and thoughtful color choices.

### The Report Is Half the Grade
> **"I nailed the technical analysis but rushed the report. Lost points on communication. Lesson learned: budget real time for writing."** — David H.

Technical correctness gets you 50% of the way. Clear, professional communication gets you the rest. Don't shortchange Phase 5.

---

---

## Common Questions (And Where to Find Answers)

### "I don't understand what a variable means."
→ Check `DATA/DATA_DICTIONARY.md` in the repository—it has detailed descriptions of every column.

### "I'm not sure what metrics to compute."
→ Re-read `RUBRIC.pdf`—it lists exactly what's required (spoiler: at least 3 metrics including delay rate).

### "I don't know how to structure my analysis."
→ Look at the USAFacts article in `SUPPLEMENTAL_MATERIALS/`—it's a model for how to present airline comparisons.

### "My code isn't working."
→ Check `README.md` for setup instructions and environment requirements. Also, the starter notebook has template code to get you started.

### "I don't know if my results are correct."
→ Compare your airline rankings to the BTS official tables in `SUPPLEMENTAL_MATERIALS/BTS_Annual_Rankings_2022_2024.pdf`. Close match = good sign.

### "I'm stuck on visualization."
→ The starter notebook (`SCRIPTS/starter_analysis.ipynb`) includes example code for bar charts and scatter plots.

### "I want to go deeper (optional modeling, advanced analysis)."
→ Great! The rubric doesn't require machine learning, but if you want to fit a logistic regression to predict delays or explore seasonal patterns, go for it. Just make sure you nail the fundamentals first.

---

## Your Mission, Restated

You work for TravelSmart, a platform helping students book flights. Your manager needs to know: **Which major U.S. airline is most likely to make students late?**

You have 18 million flight records from 2022-2024. You have the BTS 15-minute delay standard. You have official government rankings to validate against. You have all the tools you need.

**Now go find the answer—and back it up with data.** ✈️📊

---

## Ready to Dive In?

**Access the full repository here:**  
👉 **[https://github.com/davidmarip/CS3-DS4002](https://github.com/davidmarip/CS3-DS4002)**

**What's waiting for you:**
- Full dataset (or instructions to obtain it)
- Data dictionary explaining all variables
- Starter Jupyter notebook with template code
- Helper functions to speed up your analysis
- Supplemental readings (USAFacts article, BTS rankings)
- Detailed rubric showing exactly what's expected

**Read the rubric first.** Then explore the data. Then build your scorecard. **You've got this.**

---

### About This Case Study

**Created by:** David Marip, University of Virginia  
**Course:** DS4002 (Data Science Project Course)  
**Data Source:** U.S. Bureau of Transportation Statistics (BTS), 2022-2024  
**Target Audience:** 2nd-year undergraduate students with basic data science skills  
**Skills Practiced:** Data manipulation, aggregation, visualization, validation, professional communication

---

*Good luck, and may your flights always be on time!* 🎉✈️
