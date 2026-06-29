import os, json
from flask import Flask, jsonify, render_template

app = Flask(__name__)
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

def load_json(name):
    path = os.path.join(DATA_DIR, name)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/<name>')
def api_data(name):
    try:
        return jsonify(load_json(name + '.json'))
    except:
        return jsonify({'error': 'not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

