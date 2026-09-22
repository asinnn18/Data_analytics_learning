import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv(
    "../Day-02-Data-Cleaning/cleaned_retail_sales.csv"
)

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

# Calculate total sales
df["Total_Sales"] = (
    df["Quantity"] * df["Unit_Price"]
)

print("===== STATISTICAL SUMMARY =====")
print(df.describe())

# Sales by category
category_sales = (
    df.groupby("Category")["Total_Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n===== SALES BY CATEGORY =====")
print(category_sales)

# Quantity sold by category
category_quantity = (
    df.groupby("Category")["Quantity"]
      .sum()
      .sort_values(ascending=False)
)

print("\n===== QUANTITY BY CATEGORY =====")
print(category_quantity)

# Payment method usage
print("\n===== PAYMENT METHODS =====")
print(df["Payment_Method"].value_counts())

# Daily sales
daily_sales = (
    df.groupby("Date")["Total_Sales"]
      .sum()
)

print("\n===== DAILY SALES =====")
print(daily_sales.head())

# Correlation
print("\n===== CORRELATION =====")
print(df.corr(numeric_only=True))

# Visualization
category_sales.plot(kind="bar")

plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
