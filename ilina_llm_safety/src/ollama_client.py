import requests

ollama_url = "http://127.0.0.1:11434/api/generate"
model_name = "llama2"

def query_model(prompt):
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(ollama_url, json=payload)
    response.raise_for_status()

    data = response.json()
    return data["response"]

if __name__ == "__main__":
    test_prompt = "Explain what AI safety means in simpler terms."
    output = query_model(test_prompt)
    print(output)
