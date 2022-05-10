import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')


class logit(object):
    def __init__(self, logger, level):
        self.logger = logger
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            self.logger.log(self.level, 'Entering %s' % func.__name__)
            try:
                return func(*args, **kwargs)
            finally:
                self.logger.log(self.level, 'Exited %s' % func.__name__)
        return wrapper


def main(args):
    #logging.basicConfig(level=logging.INFO)
    #logging.info("Starting tool.")
    # store the original arguments
    var = sys.argv

    # check to make sure there is at least one filename to process
    if len(sys.argv) == 0:
        print ("Error: No filename provided.")
        exit(0)

    # now read each filename passed in
    #for arg in sys.argv:
    #   
