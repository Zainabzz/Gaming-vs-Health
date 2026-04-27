import pandas as pd
import os

# 1. Use the local file you already downloaded
csv_filename = "gaming_mental_health_balanced_sample_1000.csv"

if os.path.exists(csv_filename):
    print(f"Reading {csv_filename}...")
    df = pd.read_csv(csv_filename)
    
    # 2. Convert it to the JSON format your website expects
    # We name it 'dataset.json' to match your index.html
    df.to_json("dataset.json", orient="records")
    print("Success! Created 'dataset.json' with 1,000 real records.")
else:
    print(f"Error: Could not find {csv_filename} in this folder.")