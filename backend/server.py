from flask import Flask, jsonify, request
from backend.langgraph_agent import MasterAgent

backend_app = Flask(__name__)

@backend_app.route('/', methods=['GET'])
def index():
    return jsonify({"status": "Running"}), 200

@backend_app.route('/scrape_jobs', methods=['POST'])
def scrape_jobs():
    data = request.json
    master_agent = MasterAgent()
    jobs = master_agent.run(data["keywords"], data["location"])
    return jsonify({"jobs": jobs}), 200
