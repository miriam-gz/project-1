import requests
import logging

class StockFetcher:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_stock_price(self, symbol):
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={self.api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if "Time Series (1min)" in data:
                last_timestamp = list(data["Time Series (1min)"])[0]
                price = data["Time Series (1min)"][last_timestamp]["1. open"]
                return price
            else:
                logging.warning(f"No data available for {symbol}")
                return None
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching data for {symbol}: {e}")
            return None
