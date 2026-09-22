Day 1 — Understanding a Retail Sales Dataset

 Objective:

Today I learned how to inspect and understand a dataset before performing any analysis.

Instead of starting with charts or machine learning models, the first step is to understand what the data actually represents.

 Real-World Scenario:

Imagine I am working as a Junior Data Analyst for a retail company.

The company has thousands of sales transactions and wants to understand its business performance.

A transaction might look like:

Transaction ID| Date| Product Category| Quantity| Unit Price| Payment Method
10001| 2026-01-05| Electronics| 2| 25000| Card
10002| 2026-01-05| Clothing| 3| 1200| UPI
10003| 2026-01-06| Grocery| 5| 350| Cash

Before answering business questions, I first need to understand the structure and quality of this data.

---

1. Understanding Rows and Columns

Each row represents one transaction.

Each column represents a feature or attribute of that transaction.

For example:

1 row = 1 sales transaction

Date        → When the transaction happened
Category    → What type of product was purchased
Quantity    → Number of items purchased
Unit Price  → Price of one item
Payment     → Payment method used

---

2. Loading the Dataset

I used Pandas to load the CSV file.

import pandas as pd

df = pd.read_csv("retail_sales.csv")

---

3. Inspecting the First Records

print(df.head())

"head()" helps me quickly understand what the dataset looks like.

---

4. Checking Dataset Size

print(df.shape)

The result is represented as:

(rows, columns)

For example:

(10000, 8)

means the dataset contains 10,000 records and 8 columns.

---

5. Understanding Data Types

print(df.info())

This helps identify whether columns contain:

- integers
- decimal numbers
- text
- dates
- boolean values

Correct data types are important because they determine how the data can be analysed.

---

6. Checking Missing Values

print(df.isnull().sum())

This tells me how many values are missing in each column.

For example:

Customer_ID       0
Date              0
Category          3
Quantity          0
Unit_Price        5
Payment_Method    2

Missing values need to be investigated before analysis.

---

7. Checking Duplicate Transactions

print(df.duplicated().sum())

Duplicate transactions can cause incorrect sales totals.

For example, if the same ₹25,000 transaction appears twice, the company's calculated revenue could become artificially high.

---

💡 Key Learning

I learned that data analysis does not begin with creating dashboards.

The first step is:

Raw Data
   ↓
Understand Structure
   ↓
Check Data Types
   ↓
Check Missing Values
   ↓
Check Duplicates
   ↓
Clean Data
   ↓
Analyse Data

 Business Connection:

A Data Analyst should understand what each column means and whether the data can be trusted before using it to answer business questions.

 Tools Used:

- Python
- Pandas
- VS Code / Jupyter
- GitHub

 
