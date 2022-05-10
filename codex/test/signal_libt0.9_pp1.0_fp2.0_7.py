import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

from datetime import datetime
from multiprocessing import Pool
from random import sample
from time import sleep
from sys import stderr
from sys import stdout
from threading import Thread

from .stderr_logger import StderrLogger
from .utils import time_iterator

import numpy as np

class Cache(object):
    """
    A simple file cache for the conversion process
    """

    def __init__(self):
        self.log = StderrLogger()

    def get_file_path(self, path):
        splitted = list(os.path.split(path))
        directory = splitted[:-1]
        file_name = os.path.join(*directory, 'cached_'+splitted[-1])
