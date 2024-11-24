from flask import Flask, request, render_template
# from transformers import pipeline

app = Flask(__name__)

# tts_pipeline = pipeline("text-to-speech", model="coqui/XTTS-v2")

@app.route('/')
def home():
    return render_template('index.html')
