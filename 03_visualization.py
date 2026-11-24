import pandas as pd
import matplotlib.pyplot as plt
import os

#create chart folder

os.makedirs("charts", exist_ok =True)

#load analysis data
df = pd.read_csv("gold_daily_analysis.csv")
monthly = pd.read_csv("gold_monthly_average.csv")

df["price_date"] = pd.to_datetime(df["price_date"])

#chart 1: Daily Gold Price Trend

plt.figure(figsize=(12,6))

for purity in [999,995]:
    temp =df[df["gold_purity"] == purity]
    plt.plot(
        temp["price_date"],
        temp["price_inr_per_gram"],
        label = f"Gold {purity}"
    )

    plt.title("Daily Gold Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Price(INR per gram)")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("charts/daily_gold_trend.png")
    plt.show()

    #chart 2: Monthly Average Price
    plt.figure(figsize =(12,6))

    for purity in [999, 995]:
        temp = monthly[monthly["gold_purity"] == purity]
        plt.plot(
            temp["month"],
            temp["price_inr_per_gram"],
            marker ="o",
            label = f"Gold {purity}"
        )

        plt.title("Monthly Average Gold Price")
        plt.xlabel("Month")
        plt.ylabel("Average Price (INR per gram)")
        plt.legend()
        plt.tight_layout()
        plt.savefig("charts/monthly_gold_average.png")
        plt.show()

        #chart 3: Daily Percentage Change
        plt.figure(figsize = (12, 6))

        for purity in[999, 995]:
            temp = df [df["gold_purity"] == purity]
            plt.plot(
                temp["price_date"],
                temp["daily_change_pct"],
                label = f"Gold {purity}"
            )

            plt.title("DAily Gold Price Percentage Change")
            plt.xlabel("Date")
            plt.ylabel("Daily change(%)")
            plt.legend()
            plt.xticks(rotation = 45)
            plt.tight_layout()
            plt.savefig("charts/daily_percentage_change.png")
            plt.show()

            print("All charts created successfully!")