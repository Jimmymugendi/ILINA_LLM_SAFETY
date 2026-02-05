import csv
from utils.prompt_loader import load_prompts
from ollama_client import query_model

PROMPT_FILE = "prompts/perturbed_prompts.json"
OUTPUT_FILE = "results/responses.csv"

def run_experiment():
    prompts = load_prompts(PROMPT_FILE)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["base_id", "prompt", "response"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()

        for p in prompts:
            response = query_model(p["prompt"])
            writer.writerow({
                "base_id": p["base_id"],
                "prompt": p["prompt"],
                "response": response
            })

    print("Experiment complete. Results saved to results/responses.csv")

if __name__ == "__main__":
    run_experiment()
