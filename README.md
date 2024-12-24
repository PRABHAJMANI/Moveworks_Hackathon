
# Moveworks Hackathon

This repository contains a chatbot application modified to integrate **Chat Ollama** as its conversational AI model. The integration replaces the existing models with Chat Ollama's capabilities.

## Features

- **Interactive Chat:** The chatbot can respond to user queries using Chat Ollama.
- **Streamlit Integration:** The application is built using Streamlit for a user-friendly interface.
- **Chat History:** Maintains a history of chat messages for continuity.
- **Efficient Responses:** Utilizes Chat Ollama's lightweight API for real-time conversational responses.

## File Descriptions

### 1. `app.py`
The main application file that initializes the chatbot using Streamlit. It handles:
- User input through a chat interface.
- Interaction with the Chat Ollama API to generate responses.
- Displaying chat history.

### 2. `answer.py`
Contains the core function `get_answer`, which:
- Sends user prompts to the Chat Ollama API.
- Retrieves responses and formats them appropriately.

### 3. `cohere1.py`
A standalone script to test Chat Ollama integration via terminal:
- Allows up to 10 chat turns.
- Maintains a simple chat history for better context in conversations.

### 4. `cohere_embed.py`
Placeholder for embedding functionality (not modified in this version).

## Setup Instructions

1. **Install Dependencies**
   Ensure you have Python 3.8+ installed. Use the following command to install required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. **Test the Terminal Script**
   Execute the terminal-based chatbot:
   ```bash
   python cohere1.py
   ```

4. **API Configuration**
   Update the `ollama_base_url` in `answer.py` and `cohere1.py` to point to your Chat Ollama endpoint.

## Requirements

- Python 3.8+
- Streamlit
- Requests library for HTTP requests
- Chat Ollama API access

## Usage

- Open the Streamlit app and interact with the chatbot.
- Use the terminal-based script (`cohere1.py`) for testing conversational responses.

## Notes

- Ensure the Chat Ollama server is running and accessible at the configured URL.
- Update the API key and model name in the scripts as necessary.
