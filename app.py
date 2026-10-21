from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from main import VendixAIAgent
import os

app = Flask(__name__, static_folder='frontend')
CORS(app)
agent = VendixAIAgent()

@app.route('/')
def home():
    return send_from_directory('frontend', 'index.html')

@app.route('/api/run', methods=['POST'])
def run_governance():
    data = request.json or {}
    human_override = data.pop('human_override', False)
    result = agent.run_governance_pipeline(data, human_override=human_override)
    return jsonify(result)

@app.route('/health')
def health():
    return jsonify({"status": "VENDIX AI Live", "version": "2.0.0", "rules": 12})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
