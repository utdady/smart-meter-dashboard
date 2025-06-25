import pandas as pd

df = pd.read_csv("smart_meter_data.csv")

# Check for missing values
missing = df.isnull().sum()

# Check for duplicates
duplicates = df.duplicated().sum()

# Outlier detection (simple z-score)
from scipy.stats import zscore
df["z_kWh"] = zscore(df["kWh"])
outliers = df[(df["z_kWh"] > 3) | (df["z_kWh"] < -3)]

# Summary
print("Validation Summary:")
print(f"Total records: {len(df)}")
print(f"Missing values:\n{missing}")
print(f"Duplicate records: {duplicates}")
print(f"Outliers detected: {len(outliers)}")

# Export anomaly data
outliers.to_csv("outliers.csv", index=False)
