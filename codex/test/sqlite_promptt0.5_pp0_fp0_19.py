import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/Users/zheng/Desktop/test.db')

class AnsiColor:
    """
    A class for ANSI color code.
    """
    def __init__(self):
        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'

class Logger:
    """
    A class for logging.
    """
    def __init__(self, log_file):
        self.log_file = log_file
        self.logger = logging.getLogger(log_file)
        self.logger.setLevel(logging.DEBUG)
