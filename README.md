# 🥇 Gold Price Analysis & Prediction – 2026

## 📌 Project Overview

An end-to-end Data Analytics and Machine Learning project that analyzes Indian gold prices and compares prediction models for 999 and 995 gold purity.

This project uses Python, MySQL, Excel, and Power BI to perform data cleaning, exploratory data analysis, visualization, machine learning, and dashboard reporting.

## 🎯 Project Objectives

- Analyze historical gold price trends.
- Compare 999 and 995 gold prices.
- Identify daily and monthly price movements.
- Build Machine Learning models.
- Evaluate model performance using MAE, RMSE, and MAPE.
- Create an interactive Power BI dashboard.

## 🛠️ Tools & Technologies

- **Python:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- **Database:** MySQL
- **Data Analysis:** Excel, SQL
- **Visualization:** Power BI
- **Machine Learning:** Linear Regression, Random Forest
- **Version Control:** GitHub

## 📂 Project Structure

```text
Gold-Price-Prediction-2026/
│
├── Python/
│   ├── 01_mysql_connection.py
│   ├── 02_data_analysis.py
│   ├── 03_visualization.py
│   └── 04_gold_prediction.py
│
├── SQL/
│   └── Gold_Price_Prediction_2026.sql
│
├── Data/
│   ├── Gold_Daily_Data.csv
│   ├── Gold_Monthly_Data_corrected.csv
│   ├── gold_daily_analysis.csv
│   └── gold_monthly_average.csv
│
├── PowerBI/
│   └── Gold_Price_Prediction_2026.pbix
│
├── Dashboard_Screenshots/
│   └── Gold_Price_Dashboard.png
│
└── README.md
```

## 📊 Data Analysis

The project includes:

- Daily gold price analysis
- Monthly average price analysis
- Daily price changes
- Percentage change calculations
- Gold purity comparison
- Historical trend visualization

## 🤖 Machine Learning Models

Two Machine Learning algorithms were implemented:

1. Linear Regression
2. Random Forest Regressor

Separate models were trained for Gold 999 and Gold 995 using a chronological 80/20 train-test split.

### Model Evaluation Results

| Gold Purity | Model | MAE | RMSE | MAPE |
|---|---|---:|---:|---:|
| 999 | Linear Regression | 89.49 | 107.26 | 0.63% |
| 999 | Random Forest | 383.84 | 415.18 | 2.69% |
| 995 | Linear Regression | 89.03 | 106.77 | 0.62% |
| 995 | Random Forest | 380.30 | 411.19 | 2.67% |

**Best-performing model in this test:** Linear Regression for both gold purities.

These metrics represent the historical holdout test results and do not guarantee future gold prices.

## 📈 Power BI Dashboard

The dashboard includes:

- Gold 999 Average Price KPI
- Gold 995 Average Price KPI
- Gold Price Trend Comparison
- Actual vs Predicted Price Chart
- MAE, RMSE, and MAPE performance cards

## 💡 Key Insights

- Linear Regression achieved lower test errors than Random Forest for both purities.
- Gold 999 and 995 price movements followed similar historical trends.
- Model evaluation metrics help compare prediction performance.

## 🚀 Future Improvements

- Add more historical gold price data.
- Include 916 (22K) gold price analysis.
- Improve forecasting with additional time-series models.
- Develop recursive 7-day and 30-day forecasts.
- Automate data updates.

## 👩‍💻 Author

**Usha Rani M**

Aspiring Data Analyst

Skills: Python | SQL | Excel | Power BI | Machine Learning

[GitHub Profile](https://github.com/UshaDataAnalyst)

[LinkedIn Profile](https://www.linkedin.com/in/usha-rani-0b142939a/)
