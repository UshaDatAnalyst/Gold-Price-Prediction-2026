import mysql.connector
import pandas as pd
from getpass import getpass

# 1. connect to mysql
connection = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = getpass("Enter MySQL password:"),
    database = "gold_price_prediction_2026"
)

print("MySQL connected Succeessfully!")

#2. Retrive daily gold price data
query = """
SELECT
    price_date,
    gold_purity,
    price_inr_per_gram
FROM gold_daily_prices
ORDER BY price_date;
"""

df = pd.read_sql(query, connection)
connection.close()

#3. Data preparation
df["price_date"] = pd.to_datetime(df["price_date"])

df = df.dropna(
    subset = ["price_date", "gold_purity","price_inr_per_gram"]

)

#4. Display dataset information
print("\n --- DATASET OVERVIEW ---")
print(df.head())


print("\n Total Records:", len(df))
print("\n Purity-wise Records:")
print(df["gold_purity"].value_counts())

#5. Statistical analysis
print("\n -- GOLD Price STATISTICS ---")

summary = (
    df.groupby("gold_purity")["price_inr_per_gram"]
    .agg(["count", "mean", "median" , "min", "max", "std"])
    .round(2)
)

print(summary)


#6. Daily percentage change
df = df.sort_values(["gold_purity", "price_date"])

df["daily_change"] = (
    df.groupby("gold_purity")["price_inr_per_gram"].diff()
)

df["daily_change_pct"] = (
    df.groupby("gold_purity")["price_inr_per_gram"]
    .pct_change() * 100
)

#7. monthly average
df["month"] = df["price_date"].dt.to_period("M")

monthly_avg = (
    df.groupby(["month", "gold_purity"])["price_inr_per_gram"] .mean()
  
    .reset_index()
)

monthly_avg["month"] = monthly_avg["month"].astype(str)

#8. Save analysis results

df.to_csv("gold_daily_analysis.csv", index=False)
monthly_avg.to_csv("gold_monthly_average.csv", index = False)
summary.to_csv("gold_price_summary.csv")

print("\n --- MONTHLY AVERAGE ---")
print(monthly_avg)

print("\n Analysis completed  Successfully!")