import pandas as pd

df = pd.read_csv("data/raw/reviews_raw.csv")

# 1. remove duplicates
df = df.drop_duplicates(subset=["review", "bank"])

# 2. drop missing values
df = df.dropna(subset=["review", "rating"])

# 3. normalize date
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

# 4. keep required columns only
df = df[["review", "rating", "date", "bank", "source"]]

# 5. save clean dataset
df.to_csv("data/processed/reviews_clean.csv", index=False)

print("FINAL CLEAN SIZE:", len(df))
print("Missing review/rating removed.")