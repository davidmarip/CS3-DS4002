# Data Dictionary: Airline Delays 2022-2024

## Dataset Overview

**Filename:** `airline_delays_2022_2024.csv`  
**Source:** U.S. Bureau of Transportation Statistics (BTS) - Airline Service Quality Performance 234  
**Time Period:** January 2022 - December 2024  
**Records:** Approximately 18-20 million domestic flight records  
**Scope:** Major U.S. carriers, domestic flights only, excludes diverted flights

---

## Column Descriptions

### Flight Identifiers

| Column Name | Data Type | Description | Example Values |
|------------|-----------|-------------|----------------|
| `Year` | Integer | Year of flight | 2022, 2023, 2024 |
| `Month` | Integer | Month of flight (1-12) | 1, 6, 12 |
| `DayofMonth` | Integer | Day of month (1-31) | 15, 28 |
| `DayOfWeek` | Integer | Day of week (1=Monday, 7=Sunday) | 1, 5 |
| `FlightDate` | Date | Full date of flight | 2023-06-15 |
| `Carrier` | String | Two-letter airline code | AA, DL, WN |
| `CarrierName` | String | Full airline name | American Airlines, Delta Air Lines |
| `TailNum` | String | Aircraft tail number | N12345 |
| `FlightNum` | Integer | Flight number | 1234 |

### Airport Information

| Column Name | Data Type | Description | Example Values |
|------------|-----------|-------------|----------------|
| `Origin` | String | Three-letter origin airport code | ATL, ORD, LAX |
| `OriginCityName` | String | Origin city and state | Atlanta, GA |
| `Dest` | String | Three-letter destination airport code | JFK, DFW, SFO |
| `DestCityName` | String | Destination city and state | New York, NY |

### Scheduled Times

| Column Name | Data Type | Description | Example Values |
|------------|-----------|-------------|----------------|
| `CRSDepTime` | Integer | Scheduled departure time (HHMM) | 1430 (2:30 PM) |
| `CRSArrTime` | Integer | Scheduled arrival time (HHMM) | 1730 (5:30 PM) |
| `CRSElapsedTime` | Float | Scheduled flight time (minutes) | 180.0 |

### Actual Times

| Column Name | Data Type | Description | Example Values |
|------------|-----------|-------------|----------------|
| `DepTime` | Float | Actual departure time (HHMM) | 1445.0, NaN (if cancelled) |
| `ArrTime` | Float | Actual arrival time (HHMM) | 1755.0, NaN (if cancelled) |
| `ActualElapsedTime` | Float | Actual flight time (minutes) | 190.0, NaN (if cancelled) |

### Delay Metrics (in minutes)

| Column Name | Data Type | Description | Example Values | Notes |
|------------|-----------|-------------|----------------|-------|
| `DepDelay` | Float | Departure delay in minutes | 15.0, -5.0, NaN | Negative = early |
| `DepDelayMinutes` | Float | Departure delay (0 if early) | 15.0, 0.0, NaN | Min value = 0 |
| `ArrDelay` | Float | Arrival delay in minutes | 25.0, -3.0, NaN | Negative = early |
| `ArrDelayMinutes` | Float | Arrival delay (0 if early) | 25.0, 0.0, NaN | Min value = 0 |

### **Key Binary Indicators** ⭐

| Column Name | Data Type | Description | Example Values | **IMPORTANT** |
|------------|-----------|-------------|----------------|---------------|
| `ArrDelay15` | Integer | Arrival delay ≥15 minutes | 0, 1 | **PRIMARY METRIC**: 1 = late per BTS standard |
| `DepDelay15` | Integer | Departure delay ≥15 minutes | 0, 1 | 1 = departed ≥15 min late |
| `Cancelled` | Integer | Flight was cancelled | 0, 1 | 1 = cancelled |
| `Diverted` | Integer | Flight was diverted | 0, 1 | 1 = diverted (should be 0 in this dataset) |

### Delay Causes (in minutes)

When a delay occurs, airlines report the cause. These columns show minutes attributed to each category:

| Column Name | Data Type | Description | Example Values |
|------------|-----------|-------------|----------------|
| `CarrierDelay` | Float | Delay due to airline (maintenance, crew, etc.) | 20.0, NaN |
| `WeatherDelay` | Float | Delay due to weather | 15.0, NaN |
| `NASDelay` | Float | Delay due to National Aviation System (air traffic control, airport operations) | 10.0, NaN |
| `SecurityDelay` | Float | Delay due to security issues | 5.0, NaN |
| `LateAircraftDelay` | Float | Delay due to previous flight of same aircraft being late | 30.0, NaN |

**Note:** Delay cause columns are only populated for flights with `ArrDelay > 0`. If a flight is on-time or early, these will be `NaN` or 0.

### Distance

| Column Name | Data Type | Description | Example Values |
|------------|-----------|-------------|----------------|
| `Distance` | Float | Distance between airports (miles) | 1200.0 |
| `DistanceGroup` | Integer | Distance group code (1-11) | 5 |

---

## Important Notes

### Missing Values

- **Cancelled flights** have `NaN` for actual times and delay minutes
- **Delay cause** columns are only populated when `ArrDelay > 0`
- Some older records may have missing tail numbers or city names

### Key Definitions

**On-Time Performance (BTS Standard):**
> A flight is considered **on-time** if it arrives **less than 15 minutes** after its scheduled arrival time.

This means:
- `ArrDelay15 = 0` → Flight is **on-time** (arrived early or <15 min late)
- `ArrDelay15 = 1` → Flight is **delayed** (arrived ≥15 min late)

**Delay Rate for an Airline:**
```
Delay Rate = (Number of flights with ArrDelay15=1) / (Total flights) × 100%
```

**On-Time Rate for an Airline:**
```
On-Time Rate = (Number of flights with ArrDelay15=0) / (Total flights) × 100%
```

Note: On-Time Rate + Delay Rate = 100% (assuming cancelled flights are excluded)

### Airlines in Dataset

| Code | Airline Name |
|------|--------------|
| AS | Alaska Airlines |
| AA | American Airlines |
| DL | Delta Air Lines |
| F9 | Frontier Airlines |
| HA | Hawaiian Airlines |
| B6 | JetBlue Airways |
| WN | Southwest Airlines |
| NK | Spirit Airlines |
| UA | United Airlines |

### Data Filters Applied

This dataset includes:
- ✅ Domestic U.S. flights only
- ✅ Major passenger carriers (9 airlines)
- ✅ Years 2022, 2023, 2024
- ✅ Non-diverted flights

This dataset excludes:
- ❌ International flights
- ❌ Regional carriers / commuter airlines
- ❌ Cargo-only flights
- ❌ Diverted flights
- ❌ Years before 2022

---

## Example Usage

### Load the data (Python)
```python
import pandas as pd

# Load dataset
df = pd.read_csv('airline_delays_2022_2024.csv')

# Basic info
print(f"Total flights: {len(df):,}")
print(f"Date range: {df['FlightDate'].min()} to {df['FlightDate'].max()}")
print(f"Airlines: {df['CarrierName'].nunique()}")
```

### Compute delay rate by airline
```python
# Exclude cancelled flights
df_completed = df[df['Cancelled'] == 0].copy()

# Calculate delay rate for each airline
delay_rates = df_completed.groupby('CarrierName').agg(
    total_flights=('ArrDelay15', 'count'),
    delayed_flights=('ArrDelay15', 'sum')
).reset_index()

delay_rates['delay_rate_pct'] = (
    delay_rates['delayed_flights'] / delay_rates['total_flights'] * 100
)

# Sort by worst performer
delay_rates_sorted = delay_rates.sort_values('delay_rate_pct', ascending=False)
print(delay_rates_sorted)
```

---

## Data Quality Notes

- **Completeness:** Dataset is ~98% complete for key delay metrics
- **Accuracy:** Data is reported directly by airlines to BTS per federal requirements
- **Timeliness:** Data is typically published 2-3 months after the flight month
- **Consistency:** BTS applies validation rules to ensure airline reporting follows standards

---

## Questions?

If you're unsure about a variable:
1. Check the BTS documentation: https://www.bts.gov/topics/airline-time-tables
2. Look at the supplemental materials (`SUPPLEMENTAL_MATERIALS/REFERENCES.md`)
3. Inspect a few rows using `df.head()` or `df.sample(10)`

**Remember:** The most important column for this case study is `ArrDelay15` - this tells you whether each flight made someone late! 🕐✈️
