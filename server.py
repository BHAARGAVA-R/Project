from flask import Flask, jsonify
import json
import threading
import time

app = Flask(__name__)

# Global variable to store the latest location
latest_location = {"latitude": 0.0, "longitude": 0.0}

def update_location():
    global latest_location
    while True:
        try:
            with open("latest_gnss.json") as f:
                data = json.load(f)
                latest_location = {
                    "latitude": data["latitude"],
                    "longitude": data["longitude"]
                }
        except Exception as e:
            print(f"Error reading GNSS file: {e}")
        time.sleep(1)  # Update every second

# Start background thread to read GNSS data
threading.Thread(target=update_location, daemon=True).start()

@app.route('/location', methods=['GET'])
def get_location():
    return jsonify(latest_location)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
