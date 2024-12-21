from flask import Flask, request, jsonify, send_from_directory
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/run_model', methods=['POST'])
def run_model():
    data = request.json
    prompt = data.get('prompt', '')

    command = ['ollama', 'run', 'dolphin-llama3:8b']
    result = subprocess.run(command, input=prompt, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    output = result.stdout
    print(output)
    return jsonify({"output": output})

if __name__ == '__main__':
    app.run(debug=True)