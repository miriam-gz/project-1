import time
import logging

class StockMonitor:
    def __init__(self, stock_fetcher, interval=30):
        self.stock_fetcher = stock_fetcher
        self.interval = interval

    def monitor(self, symbol):
        while True:
            price = self.stock_fetcher.get_stock_price(symbol)
            if price is not None:
                logging.info(f"Current price of {symbol}: {price}")
            time.sleep(self.interval)
