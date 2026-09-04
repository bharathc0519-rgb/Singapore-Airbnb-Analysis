# Singapore Airbnb Market Analysis

End-to-end data analytics project on 2,592 active Airbnb listings across Singapore — from raw data cleaning to an interactive Power BI dashboard.

![Dashboard Banner](dashboard_banner.png)

## Project Overview

Singapore's limited land area, high tourism volume, and strict short-term rental regulations make its Airbnb market a good case study in urban pricing. This project looks at:

- Which regions and room types command the highest prices, and why
- Whether Superhost status actually pays off, in price and in demand
- Whether price predicts guest satisfaction
- Whether the market is oversupplied relative to demand

Full write-up: [Insights_and_Recommendations.docx](Insights_and_Recommendations.docx)

## Repository Structure

```
├── data/
│   └── listings_cleaned.csv          # Cleaned dataset (2,592 rows, 43 columns)
├── scripts/
│   ├── 01_data_cleaning.py           # Raw to cleaned pipeline (pandas)
│   └── 02_load_to_mysql.py           # Loads cleaned data into MySQL
├── sql/
│   └── business_questions.sql        # Business questions answered in SQL
├── excel/
│   └── listings_cleaned.xlsx         # PivotTable validation
├── dashboard/
│   └── Singapore_Airbnb_Dashboard.pbix
├── Insights_and_Recommendations.docx
└── README.md
```

## Tools Used

- Python (pandas) — cleaning, feature engineering, exploratory analysis
- MySQL — relational storage, SQL-based validation
- Excel — PivotTable cross-checks
- Power BI — interactive dashboard

## Data Cleaning

Source: Inside Airbnb, Singapore (listings, reviews, calendar, neighbourhoods).

- Raw dataset: 3,097 listings, 90 columns. Cleaned to 2,592 listings, 43 columns.
- Removed rows with missing price (16.3% of raw data)
- Standardised currency, boolean, and date fields
- Converted the free-text amenities field into an amenity count
- Dropped columns that were 100% empty in this data snapshot (host_since, host_response_rate, etc.)

## Key Findings

**Location drives price more than anything else.** Central Region averages $222/night vs. $41/night in the North Region, a 5x spread across five regions.

**Room type creates a similar spread.** Entire home/apt averages $313/night; shared room averages $61.

**Superhosts charge more and get more bookings.** About 16% higher prices, and roughly 2.5x more reviews than non-superhosts — the badge looks like it drives demand, not just price.

**Price doesn't predict guest satisfaction.** Correlation between price and review score across all listings is 0.017, essentially zero.

**Supply looks like it outpaces demand outside Central Region.** The average listing is available 307 of 365 days a year.

Recommendations for hosts, pricing strategy, and platform policy are in the full report linked above.

## Dashboard

The Power BI dashboard includes KPI cards (total listings, average price, average review score, estimated annual revenue), price breakdowns by region and room type, a Superhost comparison, a map of all listings, and region/room-type filters.

## Challenges

A few things broke along the way, worth noting since debugging them was most of the actual work:

- MySQL Workbench's Table Data Import Wizard silently truncated large CSV imports, stopping at 147 of 2,592 rows with no error message. Worked around this by loading the data directly with Python (pandas.to_sql + SQLAlchemy) instead.
- The amenities field was a JSON-like string with nested double quotes that broke CSV parsers. Replaced it with a simple amenity count.
- A handful of listing names started with a hyphen, which Excel and Power BI read as the start of a formula. Stripped leading punctuation during cleaning.

## Reproducing This

1. Clone the repo
2. Run `scripts/01_data_cleaning.py` on the raw Inside Airbnb export to regenerate `listings_cleaned.csv`
3. Run `scripts/02_load_to_mysql.py` to load the data into MySQL (optional)
4. Run the queries in `sql/business_questions.sql`
5. Open `dashboard/Singapore_Airbnb_Dashboard.pbix` in Power BI Desktop

---

Self-directed data analyst portfolio project.
