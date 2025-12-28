🏥 Healthcare Chatbot for Patient Support 🤖

An AI-powered healthcare chatbot built using Rasa (NLP) and OpenAI API to provide instant responses to patient queries and automate appointment scheduling through a conversational web interface.

📌 Project Overview

Patients often face delays in:

Getting responses to basic health-related questions

Booking appointments manually

Receiving support outside working hours

This chatbot solves these problems by acting as a 24×7 virtual health assistant.

🎯 Features

✅ Conversational patient support

📅 Automated appointment booking (date & time collection using forms)

🧠 NLP-based intent classification & entity extraction

🤖 AI-powered FAQ handling using OpenAI API

🌐 Web-based chatbot interface

📊 Fallback tracking for unanswered queries

🛠️ Tech Stack
Component	Technology
Chatbot Framework	Rasa (v3.x)
NLP	Rasa NLU
AI FAQs	OpenAI API
Backend	Python
Frontend	HTML, CSS, JavaScript
Deployment	Local / Web-based
📂 Project Structure
Rasa/
│
├── actions.py              # Custom actions & OpenAI fallback
├── config.yml              # Pipeline & policies
├── domain.yml              # Intents, slots, responses, forms
├── rules.yml               # Rule-based flows
├── stories.yml             # Conversation paths
├── data/
│   ├── nlu.yml              # Training data
│
├── credentials.yml         # API & channel credentials
├── endpoints.yml           # Action server configuration
├── models/                 # Trained models
└── README.md               # Project documentation

🧠 How It Works

User greets the bot

Bot asks for the user's name and mood

If user feels unwell → offers appointment booking

Uses Rasa Forms to collect:

Appointment Date

Appointment Time

Confirms appointment with collected details

For general questions → handled via OpenAI fallback

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/Ambesh22/healthCare_Bot
cd Rasa

2️⃣ Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install rasa
pip install rasa-sdk
pip install openai

🔑 OpenAI Configuration

In actions.py, add your OpenAI API key:

import openai
openai.api_key = "YOUR_OPENAI_API_KEY"


⚠️ Important: Use Your Own API key from OpenAI.
Use environment variables for production.

🚀 Train the Model
rasa train

▶️ Run the Project
Start Action Server
rasa run actions

Start Rasa Server
rasa shell


OR for web usage:

rasa run --enable-api --cors "*"

📈 Monitoring & Improvements

Track fallback responses

Improve intent accuracy

👨‍💻 Author

Ambesh Mishra

💼 Aspiring AI / Python Developer

🔗 LinkedIn: https://linkedin.com/in/ambesh-mishra

💻 GitHub: https://github.com/Ambesh22

⭐ Support

If you find this project helpful:

🌟 Star the repository

🍴 Fork it

🛠️ Contribute improvements
