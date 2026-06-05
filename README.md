# Hybrid AI Chatbot

## Project Overview

This project is a Hybrid AI Chatbot built using Python and Flask. It combines a Rule-Based AI Engine with an LLM Fallback mechanism.

The chatbot first attempts to answer questions using predefined rules and deterministic logic. If no rule matches, the query is forwarded to an AI model.

This architecture ensures:

* Predictable responses for known intents
* Fast execution
* Reduced hallucinations
* Improved flexibility through AI integration

---

## Features

### Rule-Based Engine

* Input sanitization
* Intent matching
* Deterministic responses using if-else logic
* Greeting detection
* Learning roadmap suggestions
* Technical topic responses

### Hybrid AI Architecture

* Rule Engine as first layer
* LLM fallback for unknown queries
* Continuous conversation support

### Web Interface

* Flask backend
* HTML frontend
* CSS styling
* Interactive chat UI

### Safety Features

* Input validation
* Guardrail responses
* Controlled response generation

---

## Project Architecture

User Input

↓

Input Sanitization

↓

Rule Matching

↓

Rule Found?
├── Yes → Return Rule-Based Response
└── No → Send Query to LLM

↓

Response Display

---

## Technologies Used

* Python
* Flask
* HTML
* CSS
* Git
* GitHub

---

## Project Structure

AI_CHATBOT/

├── app.py

├── chatbot.py

├── rules.py

├── llm.py

├── requirements.txt

├── README.md

├── static/

│ └── style.css

└── templates/

└── index.html

---

## Installation

1. Clone the repository

git clone https://github.com/kanchan3145/AI_CHATBOT.git

2. Navigate to the project folder

cd AI_CHATBOT

3. Install dependencies

pip install -r requirements.txt

4. Run the application

python app.py

5. Open browser

http://127.0.0.1:5000

---

## Example Queries

* Hello
* What is Python?
* Python roadmap
* What is AI?
* Java roadmap
* What is Machine Learning?
* Explain NLP
* System Design roadmap

---

## Learning Outcomes

* Control Flow
* If-Else Logic
* Input Processing
* IPO Model
* Rule-Based AI
* Flask Development
* Git & GitHub
* Hybrid AI Systems

---

## Author

Kanchan Kumari
