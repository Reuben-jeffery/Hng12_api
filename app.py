from flask import Flask, jsonify, redirect
from flask_cors import CORS
from datetime import datetime, timezone
import os

app = Flask(__name__)
CORS(app)

@app.route('/')

def home():
    return redirect('/api')

@app.route('/api', methods=['GET'])
def get_info():
    
    email = "reubenjeffery47@gmail.com"
    
    current_datetime = datetime.utcnow().isoformat(timespec='seconds') + "Z"
    
    github_url = "https://github.com/Reuben-jeffery/Hng12_api"
    
    return jsonify({
        "email": email,
        "current_datetime": current_datetime,
        "github_url": github_url
    })
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)