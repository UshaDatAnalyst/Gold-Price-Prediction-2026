import mysql.connector
import pandas as pd
from getpass import getpass

#connect  to MySQL
connection = mysql.connector.connect(
    host ="localhost",
    user= "root",
    password = getpass("Enter MySQL passowrd:"),
    database = "gold_price_prediction_2026"
)

print ("MySQL Connected Successfully!")

#Retrive daily gold prices
query = """
SELECT 
    price_date,
    gold_purity,
    price_inr_per_10g,
    price_inr_per_gram,
    source_series
FROM gold_daily_prices
ORDER BY price_date;
"""

df = pd.read_sql(query, connection)

print("\n First 5 Records:")
print(df.head())

print("\n Dataset Information:")
print(df.info())

print("\n Toatal Records:", len(df))

connection.close()
      
