import requests
from utils.config import SCHWAB_API_KEY, SCHWAB_API_SECRET

class SchwabAPIClient:
    def __init__(self):
        self.api_key = SCHWAB_API_KEY
        self.api_secret = SCHWAB_API_SECRET
        self.base_url = 'https://api.schwab.com'  # Replace with actual base URL

    def get_stock_data(self, symbol, start_date, end_date):
        # Implement Schwab API request here
        endpoint = f'{self.base_url}/marketdata/{symbol}/pricehistory'
        params = {
            'apikey': self.api_key,
            'startDate': start_date,
            'endDate': end_date,
            # Include other required parameters
        }
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
