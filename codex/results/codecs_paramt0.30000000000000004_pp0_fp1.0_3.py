import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------
class Config:
    def __init__(self):
        self.logger = logging.getLogger('Config')
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug('Config.__init__()')
        self.logger.debug('Config.__init__() - end')

    def get_config(self, config_file):
        self.logger.debug('Config.get_config()')
        config = ConfigParser.RawConfigParser()
        config.read(config_file)
        self.logger.debug('Config.get_config() - end')
        return config

    def get_config_section(self, config, section):
        self.logger.debug('Config.get_config_section()')
        config_section = {}
        for option in config.options(section):
            config_section[option] = config.get(section, option)
        self.logger.debug('Config.get_config_section()
