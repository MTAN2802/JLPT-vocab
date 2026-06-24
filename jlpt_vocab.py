import pandas as pd
df = pd.read_csv("jlpt_vocab.csv")

# Filter rows (example)
N1 = df[df["JLPT Level"] == "N1"] #2699 words
N2 = df[df["JLPT Level"] == "N2"] #1906 words
N3 = df[df["JLPT Level"] == "N3"] #2139 words
N4 = df[df["JLPT Level"] == "N4"] #668 words
N5 = df[df["JLPT Level"] == "N5"] #718 words

counts = df["JLPT Level"].value_counts()
result = {}

for level, total in counts.items():
    full_boxes = total // 100
    remainder = total % 100

    if remainder > 50:
        boxes = full_boxes + 1
    else:
        boxes = full_boxes if full_boxes > 0 else (1 if total > 0 else 0)

    result[level] = {
        "total_words": total,
        "boxes": boxes
    }

# Print result
for level, data in result.items():
    print(level, data)


import csv
import json

# Read CSV
with open("vocab.csv", encoding="utf-8") as f:
    data = list(csv.DictReader(f))

# Convert to JSON string
json_data = json.dumps(data, ensure_ascii=False)

# Write to JS file
with open("vocab.js", "w", encoding="utf-8") as f:
    f.write(f"const vocabData = {json_data};")
