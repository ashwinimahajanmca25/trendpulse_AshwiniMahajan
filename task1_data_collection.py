# ================================
# Task 1 - TrendPulse Project
# Title: Fetch data from HackerNews API
# ================================

# Step 0: Import libraries
import requests
import json
import os
import time
from datetime import datetime

print("Script started...")

# Step 1: API URLs
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

headers = {"User-Agent": "TrendPulse/1.0"}


# Step 2: Categories + keywords
categories = {
    "technology": ["ai", "software", "tech", "startup", "app", "programming", "data"],
    "worldnews": ["war", "government", "election", "country", "president", "global"],
    "sports": ["sport", "game", "team", "player", "league", "match"],
    "science": ["research", "study", "space", "physics", "biology", "science"],
    "entertainment": ["movie", "music", "film", "show", "netflix", "tv"]
}


# Step 3: Category function
def get_category(title):
    title = title.lower()

    for category, keywords in categories.items():
        for word in keywords:
            if word in title:
                return category

    return "others"   


# Step 4: Fetch story IDs
try:
    print("Fetching top stories...")
    response = requests.get(TOP_STORIES_URL, headers=headers)
    story_ids = response.json()[:1000]   # increased range
except Exception as e:
    print("Error fetching stories:", e)
    story_ids = []


# Step 5: Storage
all_data = []

# Category count (including others)
category_count = {
    "technology": 0,
    "worldnews": 0,
    "sports": 0,
    "science": 0,
    "entertainment": 0,
    "others": 0
}


# Step 6: Loop
for story_id in story_ids:
    try:
        res = requests.get(ITEM_URL.format(story_id), headers=headers)
        story = res.json()

        if not story or "title" not in story:
            continue

        title = story["title"]

        # Step 7: Detect category
        category = get_category(title)

        # Limit only main categories (NOT others)
        if category != "others" and category_count[category] >= 25:
            continue

        # Step 8: Extract fields
        data = {
            "post_id": story.get("id"),
            "title": title,
            "category": category,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by", "unknown"),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        all_data.append(data)
        category_count[category] += 1

        # Debug output
        print(f"Collected {len(all_data)} records")

        # Stop at 125
        if len(all_data) >= 125:
            break

        time.sleep(0.3)

    except Exception as e:
        print(f"Error in story {story_id}: {e}")
        continue


# Step 9: Create folder
if not os.path.exists("data"):
    os.makedirs("data")


# Step 10: Save file
file_name = datetime.now().strftime("data/trends_%Y%m%d.json")

with open(file_name, "w", encoding="utf-8") as f:
    json.dump(all_data, f, indent=4)


# Step 11: Final output
print("\n--- TASK 1 OUTPUT ---")
print("Data collection completed successfully")
print(f"Total records collected: {len(all_data)}")
print(f"Data saved in file: {file_name}")