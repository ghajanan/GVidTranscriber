from flask import Flask, request, jsonify,render_template,redirect, session
import fitz  # PyMuPDF
from openai import OpenAI
import time
import json
import whisper
import moviepy.editor as mp
import warnings 
import os


app = Flask(__name__)
app.secret_key = 'bdwcjvgybugxwfntfswifnrzsdbyfrncfvjj' 

@app.route('/')
def home():
     return render_template('page1.html')

@app.route('/upload')
def upload():
    return render_template('page2.html')

    
@app.route('/transcribe', methods=['POST'])
def transcribe_video():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file:
        print(f"Processing file: {file.filename}")
        # Save the video file temporarily
        filename = "temp_video.mp4"
        file.save(filename)

        # Load and transcribe the video
        video = mp.VideoFileClip(filename)
        audio_file = video.audio
        audio_file.write_audiofile("temp_audio.wav")

        warnings.simplefilter("ignore")
        model = whisper.load_model("tiny")
        result = model.transcribe(audio="temp_audio.wav", task='translate')

        # Clean up temporary files
        video.close()
        os.remove(filename)
        os.remove("temp_audio.wav")

        return jsonify({"transcript": result["text"]})

    return "Error processing file", 500


if __name__ == '__main__':
    app.run(debug=True,port=8080)
