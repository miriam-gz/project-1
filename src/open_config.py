import yaml

class ConfigLoader:
    def __init__(self, file_path='../config/config.yaml'):
        self.config = self.load_config(file_path)

    def load_config(self, file_path):
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)
