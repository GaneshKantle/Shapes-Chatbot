# Google AI Chatbot


## Overview
The **Google AI Chatbot** is a Python-based application powered by the Google Generative AI API. It allows users to interact with a conversational AI via a simple Flask web interface. This project is ideal for those learning about AI APIs, Flask web development, or integrating intelligent features into web apps.

## Features
- **Google Generative AI Integration**: Natural and intelligent conversation handling.
- **Flask Web App**: Lightweight and fast backend with a basic user interface.
- **Environment Variable Protection**: Keeps your API key secure with `.env`.
- **History**: Chat history is saved, and we can view it like other chatbots.
- **Dark/Light Theme**: We can dynamically switch the theme between dark and light for better UI/UX.

## Tech Stack
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (Minimal UI)
- **API**: Google Generative AI API

## Project Directory
```
└── ganeshkantle-shapes-chatbot/
    ├── README.md
    ├── app.py
    ├── requirements.txt
    ├── Snapshots/
    └── templates/
        └── index.html
```

## Prerequisites
- Python 3.8 or higher
- A valid Google Generative AI API key
  - [Get your API key](https://makersuite.google.com/app/apikey)

## 1. Clone this Repository
- Open your terminal
```
git clone https://github.com/GaneshKantle/Shapes-Chatbot/
cd Shapes-Chatbot
```

## 2. Create Virtual Environment
- python -m venv venv
- source venv/bin/activate  # On Windows: venv\\Scripts\\activate

## 3. Install Requirements
 ```
pip install -r requirements.txt
```

## 4. Setup .env File
- Create a file named .env and add your API key:
```
GOOGLE_API_KEY=your_api_key_here
```

## 5. Run the file
```
python app.py
```

## How It Works
- The frontend sends user input to the Flask backend.
- Flask reads the .env file to fetch the API key securely.
- A request is made to the Google Generative AI endpoint with user input.
- The response is parsed and returned to the frontend for display

## Snapshots
### User Interface of the Bot
![Screenshot 2024-12-08 101035](https://github.com/user-attachments/assets/08030e07-26e3-4f30-b462-a9117b8b20e2)

### History of Chat
![Screenshot 2024-12-08 101049](https://github.com/user-attachments/assets/ea50ed0a-0630-42c6-acf9-ad5458c6de3c)

### Dark/Light Theme
![Screenshot 2024-12-08 101123](https://github.com/user-attachments/assets/de7f6e19-2fcb-4074-8b06-5f064d049dac)


## Contributing
If you'd like to contribute, please fork the repository and submit a pull request. All contributions are welcome!

## Contact
For any queries, feel free to reach out:
- **Email:** ganeshkantle@gmail.com
- **GitHub:** (https://github.com/ganeshkantle)
- **My Bento:** (https://bento.me/kantle)
- **My Portfolio:** (https://tinyurl.com/ganeshkantle)
