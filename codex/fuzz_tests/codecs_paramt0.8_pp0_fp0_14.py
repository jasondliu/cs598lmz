import codecs
codecs.register_error("strict", codecs.ignore_errors)
config = ConfigParser.SafeConfigParser()
config.read("config.ini")

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger("main")

def robust_file_read(filename):
    try:
        with open(filename) as f:
            logger.info("reading lines from " + filename)
            return f.readlines()
    except UnicodeDecodeError:
        with codecs.open(filename, "r", "utf-8", "strict") as f:
            logger.info("reading lines from " + filename + " with strict encoding")
            return f.readlines()

class MultiprocessSentencesIterable(object):
    def __init__(self, filename, n_processes=4):
        self.filename = filename
        self.n_processes = n_processes

    def __iter__(self):
        pool = multiprocess
