import requests

class GNSSApiClient:
    def __init__(self, base_url="192.168.1.13"):
        self.base_url = base_url

    def get_latest_location(self):
        try:
            response = requests.get(f"{self.base_url}/location", timeout=5)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"API Error: {e}")
        return {"latitude": 0.0, "longitude": 0.0}
