# Fitness Chatbot

Fitness Chatbot is a Flask-based web application that serves as a virtual fitness assistant. The chatbot helps users with their fitness-related queries, provides personalized recommendations, and assists them in achieving their fitness goals.

## Features

- Personalized assistance: The chatbot asks users a series of personalization questions to understand their fitness goals, preferences, and constraints.
- Contextual responses: It uses OpenAI's GPT-3 model to provide context-aware responses based on the conversation history.
- Intuitive interface: The web interface is simple and easy to use, allowing users to interact with the chatbot seamlessly.

## Installation

1. Clone the repository:

git clone https://github.com/rv-kalamkaar/fitness-chatbot.git

2. Install dependencies:

pip install -r requirements.txt

3. Set up OpenAI API key:
   
   Sign up for OpenAI and obtain an API key. Then, set your API key as an environment variable named `OPENAI_API_KEY`.

4. Run the application:

python main_app.py


The application will be accessible at `http://localhost:5000` by default.

## Usage

1. Open the web application in your browser.
2. Start interacting with the chatbot by typing your queries or responses in the input box.
3. The chatbot will respond based on the conversation context and the provided inputs.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/my-feature`.
3. Commit your changes: `git commit -am 'Add new feature'`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Submit a pull request.

Please ensure your code follows the project's coding style and includes relevant tests.


## Acknowledgements

- OpenAI for providing the GPT-3 model used in this project.
- Flask for the web framework.
- Bootstrap for the frontend styling.

