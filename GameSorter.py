import os
import json

GAMES_DIR = "games"
OUTPUT_FILE = "games.json"

games = []

for file in os.listdir(GAMES_DIR):
    if file.endswith(".html") and file.startswith("cl"):
        filename = file[:-5]  # remove .html
        clean_name = filename[2:]  # remove "cl"

        display_name = clean_name.replace("_", " ").title()

        games.append({
            "id": clean_name,
            "name": display_name,
            "file": file
        })

# Sort alphabetically
games.sort(key=lambda x: x["name"])

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(games, f, indent=2)

print(f"Generated {OUTPUT_FILE} with {len(games)} games")
