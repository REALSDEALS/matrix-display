# Matrix - app.py (core) | REALSDEALS

## Import of Dependencies:
from flask import Flask, jsonify, send_from_directory
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__, static_folder='static')

# Serving the Front-End:
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Serving the Static Files:
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# Scrape Module:
@app.route('/api/contributions/<username>')
def get_contributions(username):
    # Fetching the 'dedicated' endpoint from the GitHub module:
    url = f"https://github.com/users/{username}/contributions"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return jsonify({"error": "User not found or GitHub blocked the request"}), 404

        soup = BeautifulSoup(response.text, 'html.parser')
        
        days = soup.find_all('td', class_='ContributionCalendar-day')
        
        contribution_data = []
        for day in days:
            date = day.get('data-date')
            level = day.get('data-level') 

            # Skipping Empty Cells (for spacing):
            if date and level:
                contribution_data.append({
                    "date": date,
                    "level": int(level)
                })
                
        return jsonify({"username": username, "contributions": contribution_data})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Listen to an available IP so Docker could route traffic:
    app.run(host='0.0.0.0', port=5000)