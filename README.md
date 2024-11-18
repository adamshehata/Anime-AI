# **Anime-AI**

Anime-AI is an anime recommendation system designed to provide personalized suggestions for anime enthusiasts. The project aims to enhance the user experience by offering a chatbot interface to interact with users, helping them discover new anime based on their preferences.

## **Current Functionality**

Currently, Anime-AI is powered by [DialoGPT (medium)](https://huggingface.co/microsoft/DialoGPT-medium) to simulate conversational responses due to limitations with the OpenAI GPT-4 API. While the primary goal of the system is to recommend anime, the current implementation acts as a placeholder chatbot for conversational interaction.

## **Features**
- **Chatbot Interaction**: Users can interact with the chatbot to explore anime recommendations or enjoy a conversational experience.
- **Flask Web App**: The application is hosted on a Flask server with a simple HTML frontend.
- **Future Goals**:
  - Integrate OpenAI GPT-4 API for enhanced recommendations.
  - Build a robust anime recommendation system using a custom dataset and advanced natural language processing (NLP) techniques.

## **How It Works**
1. **Chat Interface**: 
   - The user inputs a message through a web-based chat interface.
   - The chatbot, powered by DialoGPT, generates a response based on the input.

2. **Backend**:
   - A Flask app manages the server-side processing and connects the chatbot logic to the frontend.

3. **Frontend**:
   - A basic HTML interface is used for user interactions.

## **Technology Stack**
- **Backend**: Flask
- **NLP Model**: DialoGPT (medium)
- **Frontend**: HTML/CSS
- **Additional Tools**: PyTorch, Transformers library

## **Future Enhancements**
- Replace DialoGPT with OpenAI's GPT-4 for accurate and intelligent anime recommendations.
- Implement a comprehensive database of anime with metadata (genres, popularity, ratings, etc.).
- Add user preference tracking and analytics for improved recommendation accuracy.

## **Installation**
To set up the project locally:
1. Clone the repository:
   ```bash
   git clone https://github.com/adamshehata/Anime-AI.git
   cd Anime-AI
   ```
2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## **Contributing**
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.
