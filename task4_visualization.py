# ===============================
# Task 4 — TrendPulse Project
# Title: Visualizations
# ===============================

# Step 0 — Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# Step 1 — Load Data and Setup
# -------------------------------

# Load the cleaned CSV file from Task 3
df = pd.read_csv("data/trends_analysed.csv")

# Check first 5 rows to verify
print(df.head())

# Create outputs/ folder if it doesn't exist
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# -------------------------------
# Step 2 — Chart 1: Top 10 Stories by Score
# -------------------------------

# Sort the DataFrame by 'score' descending
top_stories = df.sort_values(by="score", ascending=False).head(10)

# Shorten titles longer than 50 characters
top_stories['short_title'] = top_stories['title'].apply(lambda x: x if len(x) <= 50 else x[:50] + "...")

# Plot horizontal bar chart
plt.figure(figsize=(10,6))
plt.barh(top_stories['short_title'], top_stories['score'], color='skyblue')
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()  # Highest score on top

# Save figure
plt.savefig("outputs/chart1_top_stories.png")
plt.show()

# -------------------------------
# Step 3 — Chart 2: Stories per Category
# -------------------------------

# Count number of stories per category
category_counts = df['category'].value_counts()

# Plot bar chart with different colours
plt.figure(figsize=(8,6))
colors = plt.cm.tab20.colors  # Use colormap for different colours
plt.bar(category_counts.index, category_counts.values, color=colors[:len(category_counts)])
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")
plt.xticks(rotation=45, ha='right')

# Save figure
plt.savefig("outputs/chart2_categories.png")
plt.show()

# -------------------------------
# Step 4 — Chart 3: Score vs Comments Scatter Plot
# -------------------------------

plt.figure(figsize=(8,6))

# Scatter plot, color by 'is_popular'
colors = df['is_popular'].map({True:'green', False:'red'})

plt.scatter(df['score'], df['num_comments'], c=colors, alpha=0.7)
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Number of Comments")

# Add legend manually
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='green', label='Popular'),
                   Patch(facecolor='red', label='Non-Popular')]
plt.legend(handles=legend_elements)

# Save figure
plt.savefig("outputs/chart3_scatter.png")
plt.show()

# -------------------------------
# Bonus — Combined Dashboard
# -------------------------------

fig, axs = plt.subplots(1, 3, figsize=(20,6))
fig.suptitle("TrendPulse Dashboard")

# Chart 1
axs[0].barh(top_stories['short_title'], top_stories['score'], color='skyblue')
axs[0].invert_yaxis()
axs[0].set_xlabel("Score")
axs[0].set_ylabel("Story Title")
axs[0].set_title("Top 10 Stories")

# Chart 2
axs[1].bar(category_counts.index, category_counts.values, color=colors[:len(category_counts)])
axs[1].set_xlabel("Category")
axs[1].set_ylabel("Count")
axs[1].set_title("Stories per Category")
axs[1].tick_params(axis='x', rotation=45)

# Chart 3
axs[2].scatter(df['score'], df['num_comments'], c=colors, alpha=0.7)
axs[2].set_xlabel("Score")
axs[2].set_ylabel("Comments")
axs[2].set_title("Score vs Comments")

# Add legend for scatter plot on the dashboard
axs[2].legend(handles=legend_elements)

plt.tight_layout(rect=[0, 0, 1, 0.95])  # leave space for suptitle
plt.savefig("outputs/dashboard.png")
plt.show()