import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import logging
import os
import errno
import pyinotify
import re
import time

LOG_LEVEL_STRINGS = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']

class LoggingLevelFilter(logging.Filter):
    """
    This is a filter which injects contextual information into the log.
    """
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        record.levelname = LOG_LEVEL_STRINGS[record.levelno // 10]
        return True

def setup_logger(name, log_file, level=logging.INFO):
    """Function setup as many loggers as you want"""
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.get
