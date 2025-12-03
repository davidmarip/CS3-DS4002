# Airline Scorecard: Which US Airline Is Most Likely to Make You Late?
### A DS4002 Case Study by David Nu Nu Marip

![Airline Performance](SUPPLEMENTAL_MATERIALS/airline_image.jpeg)

## Overview

This case study challenges you to analyze airline delay patterns using real-world data from the Bureau of Transportation Statistics. You'll determine which U.S. airline is most likely to make passengers late and validate your findings against official government benchmarks.

---

## Repository Structure

```
CS3-DS4002/
├── README.md
├── LICENSE                             
├── DATA/
│   ├── Annual Airline On-Time Rankings 2003-2024.xlsx
│   ├── DATA_DICTIONARY.md
│   └── DATA_PREPARATION.md
├── SCRIPTS/
│   ├── helper_functions.py
│   └── starter_analysis.ipynb
└── SUPPLEMENTAL_MATERIALS/
    ├── airline_image.jpeg
    └── USAFacts.pdf
```

---

## Data

The airline delay dataset should be obtained directly from the [Bureau of Transportation Statistics (BTS)](https://www.transtats.bts.gov/Tables.asp?QO_VQ=EFD). The `DATA/` folder contains:
- **DATA_DICTIONARY.md** - Complete variable definitions
- **DATA_PREPARATION.md** - Step-by-step instructions for downloading and filtering BTS data
- **Annual Airline On-Time Rankings 2003-2024.xlsx** - Official BTS rankings for validation

The dataset should include 2022-2024 domestic flight records from 9 major US carriers. Follow the preparation instructions to create your analysis dataset.

---

## Reference Materials

**USAFacts.** (2025). What are the best and worst airports and airlines for on-time performance? [https://usafacts.org/articles/what-are-the-best-and-worst-airlines-for-on-time-performance/](https://usafacts.org/articles/what-are-the-best-and-worst-airlines-for-on-time-performance/)

**Bureau of Transportation Statistics.** (2024). Annual Airline On-Time Rankings 2003-2024. [https://www.bts.gov/topics/airlines-and-airports/annual-airline-time-rankings-2003-2024](https://www.bts.gov/topics/airlines-and-airports/annual-airline-time-rankings-2003-2024)

**Bureau of Transportation Statistics.** (2024). Airline Service Quality Performance 234 (On-Time Performance). [https://www.bts.gov/topics/airline-time-tables](https://www.bts.gov/topics/airline-time-tables)

Additional reference materials are available in the `SUPPLEMENTAL_MATERIALS/` folder.
