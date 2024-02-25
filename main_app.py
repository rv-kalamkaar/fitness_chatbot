from flask import Flask, render_template, request, jsonify, redirect, url_for
import openai

app = Flask(__name__)

openai.api_key = "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"

class FitnessChatbot:
    def __init__(self):
        self.messages = []
        self.user_profile = {}
        self.end_of_conversation = False
        self.ask_personalization = True
        self.personalization_questions = [
            "What is your weight? (in kg)",
            "What is your height? (in cm)",
            "What is your fitness goal? (Choose from Strength gaining, Muscle building, Weight loss)",
            "What is your age?",
            "What is your gender? (Choose from Male or Female)",
            "Do you have any dietary restrictions?",
            "What is your body type? (Choose from Ectomorph, Mesomorph, Endomorph)"
        ]
        self.current_question_index = 0

    def generate_response(self, user_input):
        if not self.messages:
            # Greeting message
            greeting = "Hi there! I'm your fitness assistant. Let's start with your personalization."
            self.messages.append({"role": "assistant", "content": greeting})
            return greeting
        
        if self.end_of_conversation:
            return "End of conversation"
        
        if user_input.lower() == 'exit':
            self.end_of_conversation = True
            return "End of conversation"
        
        if self.ask_personalization:
            question = self.personalization_questions[self.current_question_index]
            self.current_question_index += 1
            if self.current_question_index == len(self.personalization_questions):
                self.ask_personalization = False
                question += "\nWhat is your query?"
            self.messages.append({"role": "user", "content": user_input})
            self.messages.append({"role": "assistant", "content": question})
            return question
        
        if user_input:
            self.messages.append({"role": "user", "content": user_input})
            chat = openai.chat.completions.create(
                model="gpt-3.5-turbo", messages=self.messages
            )
            reply = chat.choices[0].message.content + "\n"
            self.messages.append({"role": "assistant", "content": reply})
            return reply

chatbot = FitnessChatbot()

# Greeting message to be displayed on opening the page
@app.route('/')
def index():
    if not chatbot.messages:
        # If no messages exist, add the initial greeting message
        chatbot.messages.append({"role": "assistant", "content": "Hi there! I'm your fitness assistant. Let's start with your personalization.\n"})
    return render_template('index.html', messages=chatbot.messages)


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('user_input')
    if user_input is None:
        # Reset chat when user_input is None (e.g., page refresh)
        chatbot.messages = []
        return redirect(url_for('index'))

    response = chatbot.generate_response(user_input)
    return jsonify({"message": response})

if __name__ == '__main__':
    app.run(debug=True)
