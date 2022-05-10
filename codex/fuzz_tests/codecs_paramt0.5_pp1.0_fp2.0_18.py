import codecs
codecs.register_error('strict', codecs.ignore_errors)

def merge_dict(d1, d2):
    d = d1.copy()
    d.update(d2)
    return d

def get_config(config_path):
    with open(config_path, 'r') as f:
        config = yaml.load(f)
        return config

def get_logger(log_file, log_level=logging.INFO):
    logger = logging.getLogger()
    logger.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler(log_file)
    fh.setLevel(log_level)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

def get_data_path(config):
    if config['data_path']:
        data_path = config['data_path']
    else:

