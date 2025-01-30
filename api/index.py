from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/appi', methods=['GET'])
def get_info():
    
    email = "reubenjeffery47@gmail.com"
    
    current_time = datetime.utcnow().isoformat()
    
    github_url = "https://github.com/Reuben-jeffery/Hng12_api"
    
    return jsonify({
        "email": email,
        "current_time": current_time,
        "github_url": github_url
    })
    

if __name__ == "__main__":
    app.run(debug=True)