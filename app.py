from flask import Flask, jsonify, request, render_template
from langchain.llms import OpenAI
from flask_cors import CORS
import os

openai_api_key = os.environ.get("OPENAI_API_KEY")
#print(f"open api key is: {openai_api_key}")

app = Flask(__name__)
CORS(app)

# GET route
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# POST route
@app.route("/answer", methods=["POST", "GET"])
def answer():
    query = request.args.get("q")
    video_path = 'output.mp4'  # Path to your video file
    
    # Send the video file as the response
    return send_file(video_path, mimetype='video/mp4')


if __name__ == "__main__":
    app.run(port=9000)
