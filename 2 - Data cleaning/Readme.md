Day 2 — Cleaning Retail Sales Data

 Objective:

Today I learned how to identify and handle common data quality problems found in real-world datasets.

Real-World Scenario:

Continuing the retail analyst scenario from Day 1:

The sales team has provided a raw transaction file.

Before calculating revenue or building a dashboard, I need to make sure the data is reliable.

A raw dataset may contain:

- Duplicate transactions
- Missing values
- Incorrect data types
- Inconsistent text
- Invalid values
- Formatting problems

---

1. Inspect Missing Values

print(df.isnull().sum())

Suppose the result shows:

Customer_ID        12
Category            3
Quantity            0
Unit_Price          5
Payment_Method      2

This means different columns require different handling strategies.

We should not blindly replace every missing value with zero.

---

2. Remove Duplicate Records

First, identify duplicates:

print(df.duplicated().sum())

If duplicate records are confirmed:

df = df.drop_duplicates()

Then check again:

print(df.duplicated().sum())

The goal is to make sure the same transaction is not counted multiple times.

---

3. Handle Missing Numerical Values

For a numerical column such as "Unit_Price", the median can sometimes be used.

df["Unit_Price"] = df["Unit_Price"].fillna(
    df["Unit_Price"].median()
)

The median can be useful when extreme values may affect the average.

However, in a real company, the correct approach depends on why the value is missing and what the business data represents.

---

4. Handle Missing Categorical Values

For a categorical column such as "Payment_Method", one possible approach is using the most frequent category.

df["Payment_Method"] = df["Payment_Method"].fillna(
    df["Payment_Method"].mode()[0]
)

Again, the correct method depends on the business context.

---

5. Standardize Text Values

Suppose the category column contains:

electronics
Electronics
 ELECTRONICS

These may represent the same category.

We can standardize the text:

df["Category"] = df["Category"].str.strip().str.title()

Now the values can become:

Electronics
Electronics
Electronics

This is important because inconsistent categories can produce incorrect group-by results.

---

6. Convert Dates

A date column should be stored as a proper date type.

df["Date"] = pd.to_datetime(df["Date"])

This allows us to perform operations such as:

- Monthly sales analysis
- Daily sales trends
- Year-wise analysis
- Date filtering

---

7. Validate the Cleaned Data

After cleaning:

print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

Cleaning should always be followed by validation.

---

 Data Cleaning Workflow

Raw Retail Data
       ↓
Identify Problems
       ↓
Missing Values
       ↓
Duplicate Records
       ↓
Incorrect Data Types
       ↓
Inconsistent Values
       ↓
Clean & Transform
       ↓
Validate
       ↓
Analysis-Ready Data

 Key Learning

Data cleaning is not simply deleting rows or filling blanks.

A professional analyst needs to understand:

What is wrong? → Why is it wrong? → What is the appropriate way to fix it?

 Business Impact

If duplicate transactions remain in the dataset, revenue may be overstated.

If categories are inconsistent, category-level sales reports may be inaccurate.

If dates are stored incorrectly, monthly or yearly trends may not work properly.

Therefore, data quality directly affects business analysis.

 Tools Used

- Python
- Pandas
- VS Code / Jupyter
- GitHub



