NYC Accidents 2020 — Exploratory Data Analysis

Exploratory Data Analysis (EDA) of NYC motor vehicle collisions in 2020, completed as Task 2 for the CodeAlpha Data Analytics Internship.

Overview

This project analyzes the NYC Accidents 2020 dataset (74,881 records, 29 columns) to uncover patterns in crash frequency, timing, location, injuries/fatalities, and vehicle types. The analysis covers data cleaning, handling of missing values, and visual exploration using interactive charts.

Tools & Libraries
Python 3.13
Polars — data loading, cleaning, and aggregation
Plotly (Express & Graph Objects) — interactive visualizations

Data

The dataset (NYC Accidents 2020.csv) contains NYC motor vehicle collision records for 2020, including crash date/time, location (borough, ZIP, coordinates), injury/fatality counts, contributing factors, and vehicle types.

Note: place the CSV file inside a data/ folder (as referenced in the notebook: data/NYC Accidents 2020.csv) before running.

Data Cleaning

Removed the redundant LOCATION column (duplicated by LATITUDE/LONGITUDE).
Dropped columns with over 90% missing values (VEHICLE TYPE CODE 3–5, CONTRIBUTING FACTOR VEHICLE 3–5, OFF STREET NAME).
Dropped rows missing LATITUDE, LONGITUDE, or BOROUGH, since these are essential for spatial analysis and cannot be reliably imputed.
Filled remaining missing values in street names, contributing factors, and vehicle types with "UNKNOWN" / "Unspecified" rather than dropping further rows.
Final cleaned dataset: 47,746 rows × 21 columns.
Key Insights
January recorded the highest number of crashes among all months, accounting for 19.35% of total crashes.
January 18, 2020 was an anomalous day with 494 crashes — the highest hourly count occurred at 14:00, warranting further investigation into external factors (e.g., weather).
Brooklyn had the highest number of crashes, injuries, and fatalities among the five boroughs (5,872 injured, 26 killed), while Staten Island had the lowest.
Sedans were the most common known vehicle type involved in crashes (Vehicle 1).
Excluding "Unspecified" responses, Driver Inattention/Distraction was the most common known contributing factor for Vehicle 1, responsible for 11,900 crashes.
CONTRIBUTING FACTOR VEHICLE 2 was excluded from analysis, as ~87% of its values were either "Unspecified" or missing, offering little analytical value.

Visualizations

Line chart — crashes by month
Bar chart — crashes by borough
Density map — crash hotspots across NYC
Side-by-side bar charts — injuries and fatalities by borough

How to Run

bash
pip install polars plotly
jupyter notebook EDA.ipynb

Project Structure
.
├── EDA.ipynb              # Main analysis notebook
├── data/
│   └── NYC Accidents 2020.csv
└── README.md