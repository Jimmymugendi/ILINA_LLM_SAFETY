import json
import csv
from pathlib import Path

def load_prompts(path):
    path = Path(path)

    if path.suffix == ".json":
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        prompts = []
        for item in data:
            prompts.append({
                "base_id": item.get("base_id", item.get("id")),
                "prompt": item.get("prompt"),
                "meta": {
                    k: v for k, v in item.items()
                    if k not in ["base_id", "id", "prompt"]
                }
            })
        return prompts

    elif path.suffix == ".csv":
        prompts = []
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                prompts.append({
                    "id": row.get("base_id"),
                    "prompt": row.get("prompt"),
                    "meta": {}
                })
        return prompts

    else:
        raise ValueError("Unsupported prompt format")
