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

