import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_config(config_file):
    if not os.path.isfile(config_file):
        raise IOError('Could not locate config file: %s' % config_file)
    config = ConfigParser.SafeConfigParser()
    config.read(config_file)
    return config

def get_logger(logger_name, log_file):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return
