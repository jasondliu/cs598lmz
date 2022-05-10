import codecs
codecs.register_error('strict', codecs.ignore_errors)

#
# 
#
#
#
#
class Config(object):
    """
    Config class
    """
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = ConfigParser.ConfigParser()
        self.config.read(self.config_file)

    def get(self, section, key):
        """
        Get a value from the config file
        """
        return self.config.get(section, key)

    def get_int(self, section, key):
        """
        Get an integer value from the config file
        """
        return self.config.getint(section, key)

    def get_float(self, section, key):
        """
        Get a float value from the config file
        """
        return self.config.getfloat(section, key)

    def get_boolean(self, section, key):
        """
        Get a boolean value from the config file
        """
        return self.config.getboolean
