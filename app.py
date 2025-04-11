from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_command', methods=['POST'])
def run_command():
    data = request.get_json()
    command = data.get('command')
    if command:
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return jsonify({'output': result.stdout + result.stderr})
        except Exception as e:
            return jsonify({'output': f'Error: {str(e)}'})
    return jsonify({'output': 'No command provided'})

if __name__ == '__main__':
    app.run(debug=True)