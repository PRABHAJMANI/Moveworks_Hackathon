
import requests

def get_answer(input_text):
    ollama_base_url = "http://localhost:8000/api/chat"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "llama3.1",  
        "prompt": input_text
    }
    
    response = requests.post(ollama_base_url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("response", "No response from Chat Ollama")
    else:
        return f"Error: {response.status_code} - {response.text}"
