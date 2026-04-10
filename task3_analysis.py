# ===============================
# Task 3 — TrendPulse Project
# Title: Analysis with Pandas & NumPy
# ===============================

# Step 0: Import required libraries
import pandas as pd
import numpy as np

# -------------------------------
# Step 1 — Load and Explore
# -------------------------------

# Load the clean CSV from Task 2
df = pd.read_csv("data/trends_clean.csv")

# Print the first 5 rows to see the structure
print("First 5 rows of the data:")
print(df.head())

# Print the shape of the DataFrame (rows, columns)
print("\nData shape (rows, columns):", df.shape)

# Compute average score and average number of comments
average_score = df['score'].mean()
average_comments = df['num_comments'].mean()

print("\nAverage score   :", int(average_score))
print("Average comments:", int(average_comments))

# -------------------------------
# Step 2 — Basic Analysis with NumPy
# -------------------------------

# Convert score column to a NumPy array for analysis
scores = df['score'].to_numpy()

# Mean, median, standard deviation
mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)

print("\n--- NumPy Stats ---")
print("Mean score   :", int(mean_score))
print("Median score :", int(median_score))
print("Std deviation:", int(std_score))

# Maximum and minimum score
max_score = np.max(scores)
min_score = np.min(scores)

print("Max score    :", max_score)
print("Min score    :", min_score)

# Category with the most stories
category_counts = df['category'].value_counts()
most_stories_category = category_counts.idxmax()
most_stories_count = category_counts.max()

print("\nMost stories in:", most_stories_category, f"({most_stories_count} stories)")

# Story with the most comments
max_comments_idx = df['num_comments'].idxmax()
most_commented_title = df.loc[max_comments_idx, 'title']
most_commented_count = df.loc[max_comments_idx, 'num_comments']

print("Most commented story:", f'"{most_commented_title}" — {most_commented_count} comments')

# -------------------------------
# Step 3 — Add New Columns
# -------------------------------

# engagement = num_comments / (score + 1)
df['engagement'] = df['num_comments'] / (df['score'] + 1)

# is_popular = True if score > average_score, else False
df['is_popular'] = df['score'] > average_score

# Check the first few rows with new columns
print("\nFirst 5 rows with new columns:")
print(df.head())

# -------------------------------
# Step 4 — Save the Result
# -------------------------------

# Save the updated DataFrame to a new CSV for Task 4
df.to_csv("data/trends_analysed.csv", index=False)

print("\nSaved updated data to 'data/trends_analysed.csv'")