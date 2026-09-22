Day 1 — Dataset Basics

Objective

Understand the basic structure of a dataset and learn how to inspect data using Python and Pandas.

What I Learned

1. Dataset

A dataset is a collection of related data organized into rows and columns.

For example:

Customer| Age| City| Purchase
A| 21| Chennai| 500
B| 25| Salem| 750
C| 23| Madurai| 300

Each row represents a record, while each column represents a feature or attribute.

2. Rows and Columns

- Rows represent individual records.
- Columns represent variables/features.
- The number of rows and columns describes the basic shape of a dataset.

3. Data Types

Common data types include:

- Integer
- Float
- String
- Boolean
- Date/Time

Understanding data types is important before performing analysis.

4. Missing Values

Missing values are records where information is unavailable.

They need to be identified before analysis because they can affect the results.

5. Duplicate Records

Duplicate records are repeated rows in a dataset.

Duplicates should be checked because they may affect analysis and produce incorrect results.

Python Concepts Practiced

I used Pandas to inspect a dataset.

import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

Functions Learned

Function| Purpose
"head()"| Displays the first rows
"shape"| Returns number of rows and columns
"info()"| Shows column names and data types
"isnull()"| Identifies missing values
"sum()"| Calculates totals/counts
"duplicated()"| Identifies duplicate rows

Key Learning

Before analysing a dataset, I should first understand its structure, data types, missing values, and duplicate records.
