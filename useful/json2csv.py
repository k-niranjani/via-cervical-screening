import json
import csv
from pathlib import Path

# --- list all JSON files you want to process ---
json_paths = [
    r"G:\Jhpiego_data.v1i.coco\train\_annotations.coco.json",
    r"G:\Jhpiego_data.v1i.coco\valid\_annotations.coco.json",
    r"G:\Jhpiego_data.v1i.coco\test\_annotations.coco.json",
]

# --- mapping rules ---
cancer_map = {
    "Normal": 0,
    "Pre-cancerous": 1,
    "Cancerous": 2
}

candidacy_map = {
    "Bad-candidate": 0,
    "Good-candidate": 1
}

# --- process each JSON file ---
for json_path in json_paths:
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    rows = []
    for img in data.get("images", []):
        file_name = img["file_name"]
        tags = img.get("extra", {}).get("user_tags", [])

        # Default values
        cancer_status = 0
        candidacy = ""

        # Determine cancer status
        for tag in tags:
            if tag in cancer_map:
                cancer_status = cancer_map[tag]
            if tag in candidacy_map:
                candidacy = candidacy_map[tag]

        # if no candidacy tag present, default to blank or 0
        if candidacy == "":
            candidacy = ""

        rows.append([file_name, cancer_status, candidacy])

    # --- write CSV ---
    csv_name = Path(json_path).stem.replace("_annotations.coco", "") + "_tags.csv"
    csv_path = Path(json_path).parent / csv_name

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["image", "Cancer status", "Candidacy"])
        writer.writerows(rows)

    print(f"✅ CSV created: {csv_path}")
