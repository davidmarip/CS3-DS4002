# RUBRIC: Airline Delay Scorecard Case Study

**Assignment:** Which US Airline Is Most Likely to Make You Late?  
**Target Audience:** 2nd-year UVA Students  
**Total Points:** 100

---

## Purpose

This rubric guides your work on the airline delay scorecard case study. Your goal is to analyze real flight data, compute airline-level delay metrics, and deliver a clear, evidence-based recommendation about which airline is most likely to make travelers late.

---

## Spec Categories

### **1. Problem Understanding & Use of External Sources** (15 points)

**Goal:** Demonstrate understanding of the domain, the BTS delay standard, and how professionals present airline performance data.

| Criterion | Meets Expectations (13-15 pts) | Approaches Expectations (10-12 pts) | Does Not Meet (0-9 pts) |
|-----------|-------------------------------|-----------------------------------|----------------------|
| **BTS 15-Minute Standard** | Correctly applies BTS definition: flight is late if arrives ≥15 min after schedule. Uses `ArrDelay15` appropriately. | Minor confusion about definition but mostly applies correctly. | Does not use the 15-minute standard or applies it incorrectly. |
| **External Sources** | References USAFacts article and BTS rankings; shows understanding of how delay metrics are used in practice. | Mentions sources but doesn't engage with them meaningfully. | Does not reference external materials. |
| **Scenario Framing** | Clearly frames analysis in context of helping travelers choose airlines based on reliability. | Weak connection to scenario or real-world application. | No framing or motivation provided. |

---

### **2. Data Preparation & Exploration** (15 points)

**Goal:** Load, inspect, and prepare the dataset appropriately. Demonstrate basic understanding of the data structure and quality.

| Criterion | Meets Expectations (13-15 pts) | Approaches Expectations (10-12 pts) | Does Not Meet (0-9 pts) |
|-----------|-------------------------------|-----------------------------------|----------------------|
| **Data Loading** | Successfully loads dataset and checks dimensions, missing values, and variable types. | Loads data but minimal exploration. | Cannot load data or shows no evidence of exploration. |
| **Filtering & Cleaning** | Appropriately handles cancelled flights (excludes or reports separately); documents any sampling or filtering choices. | Some cleaning but unclear or inconsistent approach. | No data cleaning or inappropriate handling of cancelled/missing data. |
| **Summary Statistics** | Computes basic stats (e.g., total flights per airline, overall delay rate) to understand dataset. | Limited or incorrect summary stats. | No summary statistics provided. |

**Key Requirement:**  
- Student must show evidence of exploring the dataset before analysis (e.g., `.info()`, `.describe()`, checking for nulls).

---

### **3. Airline-Level Metrics & Scorecard Construction** (25 points)

**Goal:** Compute accurate, meaningful metrics for each airline. This is the core analytical task.

| Criterion | Meets Expectations (22-25 pts) | Approaches Expectations (17-21 pts) | Does Not Meet (0-16 pts) |
|-----------|-------------------------------|-----------------------------------|----------------------|
| **Delay Rate Calculation** | For each airline, correctly computes: `delay_rate = (flights with ArrDelay15=1) / (total flights) × 100%` | Delay rate computed but with minor errors or unclear methodology. | Delay rate missing or fundamentally incorrect. |
| **Multiple Metrics** | Computes **at least 3 metrics** per airline: (1) delay rate, (2) cancellation rate, (3) one additional metric (e.g., avg delay minutes for delayed flights, % of extreme delays). | Only 2 metrics computed, or metrics are incomplete. | Only 1 metric or none. |
| **Aggregation Logic** | Uses correct grouping (by airline) and aggregation functions. Results are sensible and interpretable. | Grouping/aggregation has minor issues but mostly correct. | Major errors in aggregation; results don't make sense. |

**Key Requirements:**  
- **Must compute delay rate** using `ArrDelay15` for all 9 airlines.
- **Must compute at least 3 metrics total** (delay rate + cancellation rate + 1 more).
- Results should be presented in a clear table or dataframe.

**Example Metrics:**
- Delay rate (% of flights with `ArrDelay15=1`)
- Cancellation rate (% of flights cancelled)
- Average arrival delay for delayed flights only (mean of `ArrDelayMinutes` where `ArrDelay15=1`)
- % of flights with extreme delays (≥60 minutes)
- Median delay, standard deviation, etc.

---

### **4. Visualizations & Interpretation** (20 points)

**Goal:** Create clear, professional visualizations that communicate the scorecard results. Interpret findings correctly.

| Criterion | Meets Expectations (18-20 pts) | Approaches Expectations (14-17 pts) | Does Not Meet (0-13 pts) |
|-----------|-------------------------------|-----------------------------------|----------------------|
| **Visual Quality** | At least **2 high-quality visualizations** (e.g., bar chart of delay rates, bar chart of cancellation rates). Charts have titles, axis labels, and are easy to interpret. | 1-2 visualizations but missing labels, titles, or hard to read. | No visualizations or poorly constructed charts. |
| **Visual Types** | Uses appropriate chart types (bar charts for comparisons, sorted by metric). | Chart type is functional but not optimal. | Inappropriate chart type (e.g., pie chart for 9 categories). |
| **Interpretation** | Clearly states which airline is "most likely to make you late" based on highest delay rate. Discusses patterns (e.g., "Airline X has 25% delay rate vs. Airline Y's 15%"). | Identifies worst airline but weak or vague interpretation. | Does not identify worst airline or interpretation is absent/incorrect. |

**Key Requirements:**  
- **At least 2 visualizations** comparing airlines.
- **Must identify** which airline has the highest delay rate (answers the core question).
- Visualizations should be publication-ready (clean, labeled, interpretable).

**Suggested Visuals:**
- Horizontal bar chart: Delay rate by airline (sorted)
- Horizontal bar chart: Cancellation rate by airline (sorted)
- Optional: Stacked bar for delay causes by airline
- Optional: Scatter plot (e.g., delay rate vs. cancellation rate)

---

### **5. Comparison to External Rankings** (15 points)

**Goal:** Validate findings by comparing your computed rankings to official BTS annual rankings. Discuss similarities and differences.

| Criterion | Meets Expectations (13-15 pts) | Approaches Expectations (10-12 pts) | Does Not Meet (0-9 pts) |
|-----------|-------------------------------|-----------------------------------|----------------------|
| **Comparison** | Compares student's airline ranking (by delay rate) to BTS annual rankings for the same period. Notes which airlines are similar/different. | Mentions BTS rankings but comparison is superficial. | No comparison to external rankings. |
| **Discussion of Differences** | Thoughtfully discusses why rankings might differ (e.g., student used subset of routes, different time window, sample vs. full population, domestic only). | Acknowledges differences but explanation is weak or speculative. | Does not discuss differences or incorrectly assumes results should match exactly. |

**Key Requirement:**  
- Student must reference the BTS annual rankings table (in `SUPPLEMENTAL_MATERIALS/`) and compare their top/bottom airlines to BTS's official top/bottom airlines for 2022-2024.

**Example Discussion:**
> "In my analysis, Airline X had the highest delay rate (23%), which aligns with BTS's 2023 ranking where Airline X was in the bottom 3. However, BTS shows Airline Y slightly worse than my ranking, possibly because my dataset excludes international flights and BTS includes all routes."

---

### **6. Communication & Reproducibility** (10 points)

**Goal:** Deliver a clear, professional report and reproducible analysis.

| Criterion | Meets Expectations (9-10 pts) | Approaches Expectations (7-8 pts) | Does Not Meet (0-6 pts) |
|-----------|-------------------------------|-----------------------------------|----------------------|
| **Notebook/Code** | Code is well-organized, commented, and runs without errors. Analysis is reproducible. | Code runs but is messy or poorly commented. | Code does not run or is missing key steps. |
| **Written Report** | 2-3 page report with clear sections: (1) Introduction/Question, (2) Methods/Data, (3) Results, (4) Discussion/Limitations. Professional tone and grammar. | Report is present but lacks structure or clarity. | No report or report is < 1 page / incoherent. |
| **Limitations** | Acknowledges at least 2 limitations (e.g., doesn't account for route difficulty, seasonality, small sample, excludes international). | Mentions limitations but superficially. | No discussion of limitations. |

**Key Requirements:**  
- **Jupyter notebook (or R Markdown)** must run top-to-bottom without errors.
- **Written report** must answer: (a) Which airline is most likely to make you late? (b) How do results compare to BTS? (c) What are limitations?
- Report must be **2-3 pages** (excluding figures/code).

---

## Formatting Requirements

| Item | Requirement |
|------|-------------|
| **File Types** | Notebook: `.ipynb` or `.Rmd`. Report: `.pdf` or `.docx` |
| **File Names** | Clear and descriptive (e.g., `analysis_notebook.ipynb`, `delay_scorecard_report.pdf`) |
| **Length** | Report: 2-3 pages (not including visualizations embedded in text) |
| **Visualizations** | Embedded in notebook and/or report; must be legible |
| **Code** | Must include comments explaining key steps |
| **Data** | Student should use the provided `airline_delays_2022_2024.csv`; if sampling, must document |

---

## Point Distribution Summary

| Category | Points |
|----------|--------|
| 1. Problem Understanding & Use of External Sources | 15 |
| 2. Data Preparation & Exploration | 15 |
| 3. Airline-Level Metrics & Scorecard Construction | 25 |
| 4. Visualizations & Interpretation | 20 |
| 5. Comparison to External Rankings | 15 |
| 6. Communication & Reproducibility | 10 |
| **Total** | **100** |

---

## How to Use This Rubric

1. **Before starting:** Read through all categories to understand expectations.
2. **During analysis:** Use this as a checklist. Have you computed 3+ metrics? Created 2+ visualizations? Compared to BTS?
3. **Before submitting:** Self-assess using the "Meets Expectations" column. Do you meet all criteria?

---

## Common Pitfalls to Avoid

❌ **Using the wrong delay threshold** (e.g., 10 minutes instead of 15)  
❌ **Forgetting to exclude cancelled flights** from delay rate calculation  
❌ **Only computing 1 metric** (delay rate alone is insufficient)  
❌ **No visualizations** or visualizations without labels  
❌ **Not comparing to BTS rankings**  
❌ **No discussion of limitations**  
❌ **Code that doesn't run** or missing key analysis steps  

---

## Questions?

- **Unsure about a metric?** Check the data dictionary and BTS documentation in supplemental materials.
- **Need a visual example?** Look at the USAFacts article—their bar chart is a good model.
- **Confused about comparison?** The BTS annual rankings table shows official on-time percentages by airline for each year.

---

## Final Checklist Before Submission

- [ ] Loaded and explored the dataset
- [ ] Computed delay rate for all 9 airlines using `ArrDelay15`
- [ ] Computed at least 3 metrics per airline (delay rate + cancellation rate + 1 more)
- [ ] Created at least 2 clear visualizations comparing airlines
- [ ] Identified which airline is most likely to make you late
- [ ] Compared my ranking to BTS official rankings
- [ ] Discussed why differences might exist
- [ ] Wrote a 2-3 page report with Introduction, Methods, Results, Discussion, Limitations
- [ ] Notebook runs top-to-bottom without errors
- [ ] All files named clearly and submitted per instructions

---

**Good luck! Focus on clear communication of fundamentals over fancy techniques. You've got this.** 🚀📊
