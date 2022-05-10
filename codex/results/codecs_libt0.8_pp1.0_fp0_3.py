import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

CONFIG_FILE = "config.json"

class Config:
    """
    Config class that holds the filename to load and save the config to.
    """

    def __init__(self, filename):
        """
        Initialize the Config class.
        """
        self.filename = filename
        self.config = {}

    def load(self):
        """
        Load the configuration file.
        """
        with open(self.filename, 'r') as f:
            self.config = json.load(f)

    def save(self):
        """
        Save the configuration to a file.
        """
        with open(self.filename, 'w') as f:
            json.dump(self.config, f, indent=4)

    def get_value(self, key):
        return self.config[key]

    def set_value(self, key, value):
        self.config[key] = value
        self.save()

