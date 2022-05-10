import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_logger(filename, level=logging.INFO):
    logger = logging.getLogger(filename)
    logger.setLevel(level)
    handler = logging.FileHandler(filename)
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
    logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s',level=logging.INFO)
    logger.addHandler(handler)
    return logger

def load_config(config_file):
    """
    Read config file and parse into dictionary.
    """
    config = configparser.ConfigParser()
    config.read(config_file)
    config_dict = {}

    for section in config.sections():
        config_dict[section] = {}
        for option in config.options(section):
            config_dict[section][option] = config.get(section, option)
    return config_dict

