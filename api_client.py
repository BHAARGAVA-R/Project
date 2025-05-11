import requests

class GNSSApiClient:
    def __init__(self, base_url="http://https://0a14-2404-ba00-fd01-2d33-aaf0-bae5-c326-39eb.ngrok-free.app"):
        self.base_url = base_url

    def get_latest_location(self):
        try:
            response = requests.get(f"{self.base_url}/location", timeout=5)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"API Error: {e}")
        return {"latitude": 0.0, "longitude": 0.0}
