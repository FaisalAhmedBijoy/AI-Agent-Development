from flask import Flask, request, jsonify
from ai_workflow import AIWorkflow

app = Flask(__name__)
workflow = AIWorkflow()

@app.route('/process', methods=['POST'])
def process_command():
    data = request.json
    command = data.get("command")
    if not command:
        return jsonify({"error": "Command is required."}), 400

    response = workflow.process_command(command)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
