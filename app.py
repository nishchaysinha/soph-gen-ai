import os
import json
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import core.llm as llm
import core.prompt_template as prompt_template


load_dotenv()

app = Flask(__name__)
GM = llm.GenerativeModel("gemini-pro", os.getenv("GOOGLE_API_KEY"))
chat = GM.chat_object()

@app.route('/init', methods=['POST'])
def init():
    file_structure = request.json['file_structure']
    prompt = prompt_template.init_prompt(str(file_structure))
    response = chat.send_message(prompt)
    return jsonify(response.text)


@app.route('/generate', methods=['POST'])
def generate():
    response_text = request.json['response_text']
    response_prompt = prompt_template.generate_prompt(str(response_text))
    response = chat.send_message(response_prompt)
    return jsonify(response.text)

if __name__ == "__main__":
    app.run(debug=True)
    