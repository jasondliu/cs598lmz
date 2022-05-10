import mmap
import os
import os.path
import re
import subprocess
import time

from naz import *

class Reader(object):
    """
    Abstract base class for my readers.
    """
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def readline(self):
        """
        Read a line from reading location.
        """
        raise NotImplementedError

    def readlines(self):
        """
        Read all lines from reading location.
        """
        raise NotImplementedError

    def read(self):
        """
        Read all data from reading location.
        """
        raise NotImplementedError

    def close(self):
        """
        Cleanup resources held by this reader.
        """
        raise NotImplementedError

class LineReader(Reader):
    """
    A line reader class, similar to python's built-in file objects
    """
    def __init__(self, fs, encoding, delay
