
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    mean_absolute_percentage_error
)

print("GOLD PRICE PREDICTION - ML MODEL")
print("--------------------------------")

# 1. Load dataset
df = pd.read_csv("gold_daily_analysis.csv")

print("Dataset loaded successfully!")
print("Total records:", len(df))
print("Available purities:", df["gold_purity"].unique())

df["price_date"] = pd.to_datetime(df["price_date"])
df = df.sort_values(["gold_purity", "price_date"])

all_results = []
all_predictions = []

# 2. Train separate models for 999 and 995
for purity in [999, 995]:

    print(f"\n========== GOLD {purity} ==========")

    data = df[df["gold_purity"] == purity].copy()
    data = data.sort_values("price_date")

    if len(data) < 20:
        print("Not enough records. Skipping.")
        continue

    # 3. Feature engineering
    data["day_number"] = (
        data["price_date"] - data["price_date"].min()
    ).dt.days

    for lag in [1, 2, 3, 7]:
        data[f"lag_{lag}"] = (
            data["price_inr_per_gram"].shift(lag)
        )

    data["rolling_mean_7"] = (
        data["price_inr_per_gram"]
        .shift(1)
        .rolling(7)
        .mean()
    )

    data = data.dropna().reset_index(drop=True)

    features = [
        "day_number",
        "lag_1",
        "lag_2",
        "lag_3",
        "lag_7",
        "rolling_mean_7"
    ]

    X = data[features]
    y = data["price_inr_per_gram"]

    # 4. Chronological train/test split
    split = int(len(data) * 0.8)

    X_train = X.iloc[:split]
    X_test = X.iloc[split:]

    y_train = y.iloc[:split]
    y_test = y.iloc[split:]

    print("Training records:", len(X_train))
    print("Testing records:", len(X_test))

    # 5. Machine Learning models
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(
            n_estimators=100,
            max_depth=3,
            random_state=42
        )
    }

    for model_name, model in models.items():

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        mae = mean_absolute_error(y_test, predictions)

        rmse = np.sqrt(
            mean_squared_error(y_test, predictions)
        )

        mape = mean_absolute_percentage_error(
            y_test, predictions
        ) * 100

        all_results.append({
            "Gold_Purity": purity,
            "Model": model_name,
            "MAE": round(mae, 2),
            "RMSE": round(rmse, 2),
            "MAPE_Percent": round(mape, 2)
        })

        for date, actual, predicted in zip(
            data["price_date"].iloc[split:],
            y_test,
            predictions
        ):
            all_predictions.append({
                "Date": date,
                "Gold_Purity": purity,
                "Model": model_name,
                "Actual_Price": actual,
                "Predicted_Price": predicted
            })

        print(f"\nModel: {model_name}")
        print(f"MAE: {mae:.2f}")
        print(f"RMSE: {rmse:.2f}")
        print(f"MAPE: {mape:.2f}%")

# 6. Save results
if not all_results:
    raise ValueError("No model results generated. Check dataset records.")

results_df = pd.DataFrame(all_results)
predictions_df = pd.DataFrame(all_predictions)

results_df.to_csv(
    "model_evaluation_results.csv", index=False
)

predictions_df.to_csv(
    "actual_vs_predicted.csv", index=False
)

print("\n========== MODEL COMPARISON ==========")
print(results_df.to_string(index=False))

print("\nBoth CSV result files saved successfully!")
print("MACHINE LEARNING COMPLETED!")
