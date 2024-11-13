import threading
from stock_fetcher import StockFetcher
from stock_monitor import StockMonitor

class StockService:
    def __init__(self, config, symbols):
        self.config = config
        self.symbols = symbols
        self.threads = []

    def start_service(self):
        for symbol in self.symbols:
            stock_fetcher = StockFetcher(self.config['api_key'])
            stock_monitor = StockMonitor(stock_fetcher, self.config['monitor']['interval'])
            t = threading.Thread(target=stock_monitor.monitor, args=(symbol,))
            self.threads.append(t)
            t.start()

        for t in self.threads:
            t.join()
