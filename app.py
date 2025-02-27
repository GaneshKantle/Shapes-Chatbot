import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as ai


# Load environment variables
load_dotenv()


# Ensure API key is set
API_KEY = os.getenv('GOOGLE_GEN_AI_API_KEY')
if not API_KEY:
    raise ValueError("No API key found. Please set GOOGLE_GEN_AI_API_KEY in .env file.")


# Configure the API
ai.configure(api_key=API_KEY)


# Initialize the model
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

app = Flask(__name__)

# Store chat history
chat_history = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json['message']

    # Send message to AI
    response = chat.send_message(user_message)

    # Store in chat history
    chat_history.append({
        'user': user_message,
        'bot': response.text
    })

    return jsonify({
        'response': response.text,
        'success': True
    })


@app.route('/get_history', methods=['GET'])
def get_history():
    return jsonify(chat_history)


if __name__ == '__main__':
    app.run(debug=True)