import logging

class LoggerSetup:
    def __init__(self, config):
        self.config = config
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            level=self.config['logging']['level'],
            filename=self.config['logging']['file'],
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
        console = logging.StreamHandler()
        console.setLevel(self.config['logging']['level'])
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console.setFormatter(formatter)
        logging.getLogger().addHandler(console)
