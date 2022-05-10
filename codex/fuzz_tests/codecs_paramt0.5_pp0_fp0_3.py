import codecs
codecs.register_error('strict', codecs.ignore_errors)

def init_logger(log_file):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(message)s')
    
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

def read_data(data_file):
    data = []
    with codecs.open(data_file, 'r', 'utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(line)
    return data

def read_config(config_file):
   
