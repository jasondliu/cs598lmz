import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

class Logger(object):
    """
    Wrapper class for logging.
    """
    @staticmethod
    def get_logger(filename):
        logger = logging.getLogger('logger')
        logger.setLevel(logging.DEBUG)
        logging.basicConfig(format='%(message)s', level=logging.DEBUG)
        handler = logging.FileHandler(filename)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
        logging.getLogger('logger').addHandler(handler)
        return logger

def prepro(sent):
    sent = sent.lower().strip()
    sent = re.sub('[^a-zA-Z0-9 \n\.]', '', sent)
    return sent

def format_data(data_file, out_file):
