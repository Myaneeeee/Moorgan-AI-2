from flask import Flask, request, jsonify
from openai import AzureOpenAI
from dotenv import load_dotenv
import os
from flask_cors import CORS

# Load .env variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

# Get Azure OpenAI credentials from environment
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
api_version = os.getenv("AZURE_OPENAI_VERSION")
api_key = os.getenv("AZURE_OPENAI_KEY")

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=api_key,
)

@app.route("/ask", methods=["POST"])
def ask_bot():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # Chat completion request
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are Moorgan, a helpful livestock assistant that gives insights on cattle health and farm monitoring.",
                },
                {
                    "role": "user",
                    "content": user_message,
                }
            ],
            max_tokens=1000,
            temperature=0.7,
            top_p=1.0,
            model=deployment
        )

        return jsonify({
            "response": response.choices[0].message.content
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
