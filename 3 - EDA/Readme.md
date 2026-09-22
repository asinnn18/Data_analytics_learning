Day 3 — Exploratory Data Analysis

🎯 Objective

Today I learned how to explore cleaned business data and convert raw numbers into useful observations.

🏢 Real-World Scenario

Imagine the retail company's manager asks:

«"Which product categories are performing well, and how are our sales changing?"»

Instead of manually checking thousands of transactions, I can use EDA to investigate the data systematically.

---

1. Understand Numerical Data

First, I use:

df.describe()

This provides statistics such as:

- Count
- Mean
- Standard deviation
- Minimum
- Maximum
- Quartiles

For example, if the average quantity is 3.2, it tells us approximately how many units are sold per transaction.

---

2. Calculate Total Sales

If the dataset contains:

Quantity
Unit_Price

we can calculate transaction-level sales:

df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

This converts individual transaction information into a business metric.

---

3. Find Sales by Product Category

category_sales = (
    df.groupby("Category")["Total_Sales"]
      .sum()
      .sort_values(ascending=False)
)

print(category_sales)

This helps answer:

«Which product categories generated the most revenue?»

This is more useful to a business than simply looking at raw rows.

---

4. Analyse Sales Volume

category_quantity = (
    df.groupby("Category")["Quantity"]
      .sum()
      .sort_values(ascending=False)
)

print(category_quantity)

This answers:

«Which categories sell the highest number of units?»

Revenue and quantity are different business metrics.

A category can sell many units but generate less revenue because its products have lower prices.

---

5. Analyse Payment Methods

payment_counts = df["Payment_Method"].value_counts()

print(payment_counts)

This helps understand how customers are paying.

For example:

UPI
Card
Cash

Such information can be useful for understanding customer payment behaviour.

---

6. Analyse Sales Over Time

First make sure the date is correctly converted:

df["Date"] = pd.to_datetime(df["Date"])

Then calculate daily sales:

daily_sales = (
    df.groupby("Date")["Total_Sales"]
      .sum()
)

print(daily_sales)

This helps identify sales trends over time.

---

7. Visualize Sales

import matplotlib.pyplot as plt

category_sales.plot(kind="bar")

plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

Visualization makes comparisons easier to understand.

---

8. Correlation

For numerical variables:

print(
    df.corr(numeric_only=True)
)

Correlation can help identify relationships between numerical variables.

However, correlation does not automatically mean causation.

---

🔎 Business Questions Investigated

Through EDA, I can investigate questions such as:

Question 1

Which category generates the highest revenue?

Question 2

Which category sells the most units?

Question 3

Which payment method is used most frequently?

Question 4

How does sales volume change over time?

Question 5

Are there relationships between numerical variables?

---

🔄 EDA Workflow

Clean Dataset
      ↓
Understand Variables
      ↓
Calculate Business Metrics
      ↓
Group & Aggregate
      ↓
Find Patterns
      ↓
Visualize
      ↓
Generate Business Questions

💡 Key Learning

EDA is not just about creating charts.

The main purpose is to ask useful questions about the data and investigate them systematically.

The technical result is important, but the business meaning behind the result is equally important.

🏢 Example of Business Thinking

Instead of saying:

«"Electronics has the highest sales."»

A data analyst should also ask:

- Why is it generating higher revenue?
- Is the quantity sold higher?
- Is the average selling price higher?
- Is the trend consistent over time?
- Are there seasonal patterns?

This mindset helps move from simply writing Python code to performing meaningful data analysis.

🛠️ Tools Used

- Python
- Pandas
- Matplotlib
- VS Code / Jupyter
- GitHub

 What I Learned in Day 1–3

Day 1 → Understand the Data
          ↓
Day 2 → Clean the Data
          ↓
Day 3 → Explore the Data

These are fundamental steps in a typical data analysis workflow.

