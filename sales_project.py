import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# -----------------------------
# Load Dataset
# -----------------------------
data = pd.read_csv("amazon.csv")

# Show first 5 rows
print("First 5 Rows of Dataset:")
print(data.head())

# -----------------------------
# Data Cleaning
# -----------------------------
print("\nMissing Values:")
print(data.isnull().sum())

# Remove missing values
data = data.dropna()

print("\nData cleaned successfully!")

# -----------------------------
# Show Column Names
# -----------------------------
print("\nColumn Names:")
print(data.columns)

# -----------------------------
# GRAPH 1:
# Top Product Categories
# -----------------------------
category_count = data['category'].value_counts().head(10)

plt.figure(figsize=(10,5))
category_count.plot(kind='bar')

plt.title("Top Product Categories")
plt.xlabel("Category")
plt.ylabel("Count")
plt.grid(True)
plt.savefig("Top Product Categories.png")
plt.show()

# -----------------------------
# GRAPH 2:
# Product Ratings Distribution
# -----------------------------
plt.figure(figsize=(8,5))
data['rating'].value_counts().head(10).plot(kind='bar')

plt.title("Product Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.grid(True)
plt.savefig("Product Ratings Distribution.png")
plt.show()

# -----------------------------
# GRAPH 3:
# Discount Percentage Distribution
# -----------------------------
plt.figure(figsize=(8,5))
data['discount_percentage'].value_counts().head(10).plot(kind='bar')

plt.title("Discount Percentage Distribution")
plt.xlabel("Discount Percentage")
plt.ylabel("Count")
plt.grid(True)
plt.savefig("Discount Percentage Distribution.png")
plt.show()

# -----------------------------
# GRAPH 4:
# Top Product Rating Counts
# -----------------------------
plt.figure(figsize=(8,5))
data['rating_count'].head(10).plot(kind='bar')

plt.title("Top Product Rating Count")
plt.xlabel("Products")
plt.ylabel("Rating Count")
plt.grid(True)
pit.savefig("Top Product Rating Count.png")
plt.show()

# -----------------------------
# Prediction Model
# -----------------------------
x = np.array(range(len(category_count))).reshape(-1,1)
y = category_count.values

model = LinearRegression()
model.fit(x, y)

prediction = model.predict([[10]])

print("\nPrediction Model Result:")
print("Predicted value:", prediction[0])

# -----------------------------
# Analysis Output
# -----------------------------
print("\nAnalysis:")
print("1. Cables and accessories have the highest product count.")
print("2. Most products have ratings between 4.0 and 4.3.")
print("3. Discount percentages vary across products.")
print("4. Product categories are not equally distributed.")