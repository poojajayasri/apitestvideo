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
    video_url = "https://github.com/poojajayasri/apitestvideo/blob/main/output.mp4"
    response = requests.get(video_url)
    
    if response.status_code == 200:
        with open("output.mp4", "wb") as f:
            f.write(response.content)
        
        video_path = 'output.mp4'  # Path to the downloaded video file
        
        # Send the video file as the response
        return send_file(video_path, mimetype='video/mp4')
    
    return "Video not found"



if __name__ == "__main__":
    app.run(port=5000)
