# 🚗 NYC Accidents 2020 — EDA
## 📌 Project Overview
This project was completed as part of the **CodeAlpha Data Analytics Internship**.
It performs exploratory data analysis on NYC motor vehicle collision records from 2020, using Python and Polars, and visualizes the findings with interactive Plotly charts.

---

## 🚀 Features
- Clean and preprocess raw crash data (74,881 records)
- Handle missing values with borough, coordinate, and vehicle-level strategies
- Analyze crash trends by month, date, and hour
- Compare crash, injury, and fatality counts across boroughs
- Identify most common vehicle types and contributing factors
- Visualize crash density across NYC with an interactive map

---

## 🛠 Technologies
- Python
- Polars
- Plotly (Express & Graph Objects)
- Jupyter Notebook

---

## 📁 Project Structure
```
CodeAlpha_Tasks/
│
└── Task 2 - EDA/
    ├── data/
    │   └── NYC Accidents 2020.csv
    ├── EDA.ipynb
    ├── requirements.txt
    └── README.md
```

---

## ▶️ How to Run
Install the required libraries:
```bash
pip install -r requirements.txt
```
Run the project:
```bash
jupyter notebook EDA.ipynb
```

---

## 📊 Key Insights
- **January** had the highest number of crashes, accounting for **19.35%** of the total.
- **January 18, 2020** was an anomalous day with 494 crashes, peaking at **14:00**.
- **Brooklyn** recorded the highest number of crashes, injuries (5,872), and fatalities (26); **Staten Island** had the fewest.
- **Sedans** were the most common known vehicle type involved in crashes.
- Excluding "Unspecified" values, **Driver Inattention/Distraction** was the leading known contributing factor, responsible for 11,900 crashes.

---



