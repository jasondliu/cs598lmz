import mmap
import math

"""
TODO:
- make the start() method test for the whole line to be available before
  trying to read it
"""

class LineReader():
    """
    Read data, one line at a time, from a file or other stream.
    Use it in a for loop!
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.line = ''
        self.eof = False
        self.file = None
        self.last_read = ''
        self.mmap = None
