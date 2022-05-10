import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Config(object):
    """
    Config class
    """
    def __init__(self, config_file):
        """
        Initialize config class
        """
        self.config_file = config_file
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(codecs.open(config_file, 'r', 'utf-8', 'strict'))
        self.config.read(config_file)

    def get(self, section, option):
        """
        Get config value
        """
        return self.config.get(section, option)

    def set(self, section, option, value):
        """
        Set config value
        """
        self.config.set(section, option, value)

    def write(self):
        """
        Write config
        """
        self.config.write(codecs.open(self.config_file, 'w', 'utf-8', 'strict'))

    def get_section(self, section):
       
