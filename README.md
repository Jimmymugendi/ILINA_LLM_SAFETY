# ILINA_LLM_SAFETY

This repository contains an experiment testing LLM responses to Tier-2, perturbed, and base prompts in a safety-aware context. The goal is to analyze which prompts trigger model safety filters and which generate usable outputs, focusing on defensive cybersecurity scenarios.

## Project Structure


- **prompts/** — JSON files containing different categories of prompts.  
  - `tier2_contextual_prompts.json` → high-risk Tier-2 prompts  
  - `perturbed_prompts.json` → safe, reworded prompts  
  - `base_prompts.json` → standard prompts  

- **results/** — CSV outputs from model queries.  
- **src/** — main experiment scripts and utilities.  
- **utils/** — helper modules like `prompt_loader.py` for prompt loading.

---

## How to Run

1. Clone the repository:

```bash
git clone [<YOUR_REPO_URL>](https://github.com/Jimmymugendi/ILINA_LLM_SAFETY.git)
cd ILINA_LLM_SAFETY
