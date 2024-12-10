
import requests

chat_history = []
max_turns = 10

def get_ollama_response(message):
    ollama_base_url = "http://localhost:8000/api/chat"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "llama3.1",
        "prompt": message
    }
    response = requests.post(ollama_base_url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("response", "No response from Chat Ollama")
    else:
        return f"Error: {response.status_code} - {response.text}"

for _ in range(max_turns):
    message = input("Send the model a message: ")
    answer = get_ollama_response(message)
    print("

")
    print(answer)

    user_message = {"user_name": "User", "text": message}
    bot_message = {"user_name": "Chatbot", "text": answer}
    
    chat_history.append(user_message)
    chat_history.append(bot_message)
