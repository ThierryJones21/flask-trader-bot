from flask import Flask, jsonify
import gdown
app = Flask(__name__)

@app.route('/')
def home():
    return 'I run google colabs!'

@app.route('/run')
def run_colab():
    gdown.download('https://drive.google.com/drive/u/0/folders/1cCUx3v1OnZwvpjuYRbbyTyjEjBJlBzPQ', 
                   'python-stock-predictor-alpaca-api.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')
