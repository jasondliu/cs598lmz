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
        try:
            self.file = open(file_name, 'r')
            self.mmap = mmap.mmap(self.file.fileno(), 0, access=mmap.ACCESS_READ)
            self.next()
        except IOError as e:
            print 'IOError: %s' % e

    def __del__(self):
        if self.file:
            self.file.close()
            self.file = None
        if self.mmap:
           
