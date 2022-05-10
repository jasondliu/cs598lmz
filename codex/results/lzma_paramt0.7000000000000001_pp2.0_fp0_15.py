from lzma import LZMADecompressor
LZMADecompressor()

from datetime import date
from dateutil.relativedelta import relativedelta

import csv
import re
import sys
import requests
import time

class ParseError(Exception):
    """Raised when unable to parse the given file"""
    pass

class ParseProcessor(object):
    """Processes the file and returns the parsed data as a string."""
    def __init__(self, file_path, file_name, compress = False,
            log = None, log_name = 'log'):
        if log is None:
            self.log = open(log_name, 'a')
        else:
            self.log = log
        self.file_path = file_path
        self.file_name = file_name
        self.compress = compress

    def __del__(self):
        self.log.close()

    def process(self):
        """Performs the processing of the file, returns a string of parsed data."""
        #Subclasses should override this method
        return

    def read_file(self):
        """Read
