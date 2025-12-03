# Data Preparation Instructions

## Overview

This document explains how to obtain and prepare the airline delay dataset for the case study directly from the Bureau of Transportation Statistics (BTS).

---

## Option 1: Download Directly from BTS (Recommended)

### Step 1: Access BTS Data

1. **Go to BTS website:**
   - URL: https://www.transtats.bts.gov/Tables.asp?QO_VQ=EFD

2. **Navigate to On-Time Performance Data:**
   - Select "Marketing Carrier On-Time Performance (Beginning January 2018)"
   - Choose monthly data for 2022, 2023, 2024

3. **Download monthly files:**
   - Download CSV files for each month (36 files total: Jan 2022 - Dec 2024)
   - Each file is approximately 50-150 MB
   - Save all files to a single directory (e.g., `bts_monthly/`)

### Step 2: Combine and Filter

```python
import pandas as pd
import glob
import os

# Read all monthly files from the BTS download directory
all_files = glob.glob('path/to/bts_monthly/*.csv')
df_list = []

print(f"Found {len(all_files)} monthly files to process...")

for file in all_files:
    print(f"Loading {os.path.basename(file)}...")
    df_month = pd.read_csv(file)
    df_list.append(df_month)

# Combine all months
df_full = pd.concat(df_list, ignore_index=True)
print(f"Combined dataset: {len(df_full):,} records")

# Filter to years 2022-2024
df_filtered = df_full[df_full['Year'].isin([2022, 2023, 2024])].copy()

# Filter to major carriers (9 airlines)
major_carriers = ['Alaska Airlines Inc.', 'American Airlines Inc.', 
                  'Delta Air Lines Inc.', 'Frontier Airlines Inc.',
                  'Hawaiian Airlines Inc.', 'JetBlue Airways', 
                  'Southwest Airlines Co.', 'Spirit Air Lines',
                  'United Air Lines Inc.']

df_filtered = df_filtered[df_filtered['Reporting_Airline'].isin(
    ['AS', 'AA', 'DL', 'F9', 'HA', 'B6', 'WN', 'NK', 'UA']
)].copy()

# Exclude diverted flights
if 'Diverted' in df_filtered.columns:
    df_filtered = df_filtered[df_filtered['Diverted'] == 0].copy()

# Create carrier name column from code
carrier_mapping = {
    'AS': 'Alaska Airlines Inc.',
    'AA': 'American Airlines Inc.',
    'DL': 'Delta Air Lines Inc.',
    'F9': 'Frontier Airlines Inc.',
    'HA': 'Hawaiian Airlines Inc.',
    'B6': 'JetBlue Airways',
    'WN': 'Southwest Airlines Co.',
    'NK': 'Spirit Air Lines',
    'UA': 'United Air Lines Inc.'
}

df_filtered['CarrierName'] = df_filtered['Reporting_Airline'].map(carrier_mapping)
df_filtered['Carrier'] = df_filtered['Reporting_Airline']

# Create ArrDelay15 if not present (BTS provides ArrDel15)
if 'ArrDel15' in df_filtered.columns:
    df_filtered['ArrDelay15'] = df_filtered['ArrDel15']
elif 'ArrDelayMinutes' in df_filtered.columns:
    df_filtered['ArrDelay15'] = (df_filtered['ArrDelayMinutes'] >= 15).astype(int)

# Ensure Cancelled column exists
if 'Cancelled' not in df_filtered.columns:
    df_filtered['Cancelled'] = 0

# Save filtered dataset
df_filtered.to_csv('../DATA/airline_delays_2022_2024.csv', index=False)

print(f"\n✅ Filtered dataset saved: {len(df_filtered):,} records")
print(f"Airlines: {df_filtered['CarrierName'].nunique()}")
print(f"Years: {sorted(df_filtered['Year'].unique())}")
```

---

## Option 2: Use a Sample (For Testing)

If you want to work with a smaller sample first:

```python
# Load the full filtered dataset
df_full = pd.read_csv('../DATA/airline_delays_2022_2024.csv')

# Create a stratified sample (10% of data)
df_sample = df_full.groupby('CarrierName', group_keys=False).apply(
    lambda x: x.sample(frac=0.1, random_state=42)
)

# Save sample
df_sample.to_csv('../DATA/airline_delays_sample.csv', index=False)

print(f"Sample dataset: {len(df_sample):,} records")
```

**Important:** If you use a sample, document this in your analysis and report!

---

## Required Columns

Ensure your final CSV has these columns:

### Essential:
- `Year`, `Month`, `DayofMonth`, `DayOfWeek`
- `Carrier` (2-letter code)
- `CarrierName` (full airline name)
- `Origin`, `Dest` (airport codes)
- `ArrDelayMinutes` (arrival delay in minutes)
- `ArrDelay15` (binary: 1 = ≥15 min late, 0 = on-time)
- `Cancelled` (binary: 1 = cancelled, 0 = not cancelled)

### Useful (but optional):
- `DepDelayMinutes` (departure delay)
- `CarrierDelay`, `WeatherDelay`, `NASDelay`, `SecurityDelay`, `LateAircraftDelay`
- `Distance`
- `TailNum`, `FlightNum`

---

## Data Validation Checklist

After preparing your dataset, verify:

- [ ] Years 2022, 2023, 2024 are present
- [ ] Exactly 9 major airlines included
- [ ] `ArrDelay15` column exists and is binary (0/1)
- [ ] `Cancelled` column exists and is binary (0/1)
- [ ] No diverted flights (or `Diverted` column is all 0)
- [ ] Dataset is 500K - 20M rows (depending on filtering)
- [ ] File saved to `DATA/airline_delays_2022_2024.csv`

You can run this validation code:

```python
from SCRIPTS.helper_functions import check_data_quality

df = pd.read_csv('../DATA/airline_delays_2022_2024.csv')

print(f"Records: {len(df):,}")
print(f"Years: {sorted(df['Year'].unique())}")
print(f"Airlines: {df['CarrierName'].nunique()}")
print(f"ArrDelay15 exists: {'ArrDelay15' in df.columns}")
print(f"Cancelled exists: {'Cancelled' in df.columns}")

check_data_quality(df)
```

---

## Troubleshooting

**Problem:** BTS column names differ from expected
- **Solution:** BTS uses `ArrDel15` instead of `ArrDelay15`, and `Reporting_Airline` instead of `Carrier`. The filtering script handles these mappings.

**Problem:** `ArrDelay15` column is missing
- **Solution:** Create it: `df['ArrDelay15'] = (df['ArrDelayMinutes'] >= 15).astype(int)`

**Problem:** Airline names don't match between files
- **Solution:** Standardize names or use carrier codes instead

**Problem:** Memory error when loading full dataset
- **Solution:** Use chunked reading or create a sample first

---

## Expected File Size

- **Full dataset (2022-2024, 9 airlines):** 1-3 GB
- **Sample (10%):** 100-300 MB
- **Minimal (1%):** 10-30 MB

---

## Need Help?

- Check `DATA_DICTIONARY.md` for column definitions
- Review the README.md for BTS documentation links
- Consult the `helper_functions.py` module for data loading utilities

---

**Once your data is ready, proceed to `starter_analysis.ipynb` to begin the analysis!**
