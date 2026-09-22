import pandas as pd

# Load dataset
df = pd.read_csv("retail_sales.csv")

print("===== ORIGINAL DATASET =====")
print("Rows and Columns:", df.shape)

# Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Check duplicates
print("\n===== DUPLICATES =====")
print("Duplicate rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Standardize category values
if "Category" in df.columns:
    df["Category"] = df["Category"].str.strip().str.title()

# Convert date column
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Fill numerical missing values
if "Unit_Price" in df.columns:
    df["Unit_Price"] = df["Unit_Price"].fillna(
        df["Unit_Price"].median()
    )

# Fill categorical missing values
if "Payment_Method" in df.columns:
    df["Payment_Method"] = df["Payment_Method"].fillna(
        df["Payment_Method"].mode()[0]
    )

print("\n===== AFTER CLEANING =====")
print("Rows and Columns:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

# Save cleaned dataset
df.to_csv("cleaned_retail_sales.csv", index=False)

print("\nCleaned dataset saved successfully.")
