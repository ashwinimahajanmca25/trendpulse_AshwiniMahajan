# Task 2 — TrendPulse Project
# Title: Clean the Data & Save as CSV

# Import necessary libraries
import pandas as pd


# ------------------------------
# Step 1 — Load the JSON File
# ------------------------------

# Load the JSON file exported from Task 1
json_file = "data/trends_20260410.json"  # replace with your JSON file name
df = pd.read_json(json_file)

# Print how many rows were loaded
print(f"Loaded {len(df)} stories from {json_file}")

# ------------------------------
# Step 2 — Clean the Data
# ------------------------------

# Remove duplicates based on 'post_id'
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# Drop rows with missing post_id, title, or score
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Ensure 'score' and 'num_comments' are integers
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].fillna(0).astype(int)  # fill missing comments with 0

# Remove low-quality stories (score < 5)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Strip extra whitespace from titles
df["title"] = df["title"].str.strip()

# ------------------------------
# Step 3 — Save as CSV
# ------------------------------

output_csv = "data/trends_clean.csv"
df.to_csv(output_csv, index=False)
print(f"\nSaved {len(df)} rows to {output_csv}")

# Quick summary: stories per category
print("\nStories per category:")
print(df["category"].value_counts())