from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Initialize Flask app
app = Flask(__name__)

# Initialize tokenizer and model with error handling
try:
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
except Exception as e:
    print(f"Error loading model or tokenizer: {e}")
    tokenizer, model = None, None

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    try:
        # Ensure the 'msg' parameter is in the request
        msg = request.form.get("msg", "")
        if not msg:
            return jsonify({"error": "Message is required"}), 400

        # If model is not loaded, return error
        if tokenizer is None or model is None:
            return jsonify({"error": "Model not available. Please try again later."}), 500

        # Get the response from the model
        response = get_Chat_response(msg)
        return jsonify({"response": response})
    
    except Exception as e:
        # General error handling
        print(f"Error in /get route: {e}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

def get_Chat_response(text):
    try:
        # Initialize chat_history_ids
        chat_history_ids = torch.tensor([]).long().unsqueeze(0)  # Empty tensor to store the chat history

        # Let's chat for 5 lines
        for step in range(5):
            # Encode the new user input, add the eos_token, and return a tensor in Pytorch
            new_user_input_ids = tokenizer.encode(str(text) + tokenizer.eos_token, return_tensors='pt')

            # Append the new user input tokens to the chat history
            bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

            # Generate a response while limiting the total chat history to 1000 tokens
            chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

        # Return the bot's last output token after the loop
        return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    
    except Exception as e:
        # Error handling for any issues inside the chat response generation
        print(f"Error generating chat response: {e}")
        return "Sorry, there was an error generating the response. Please try again."

if __name__ == '__main__':
    app.run(debug=True)
