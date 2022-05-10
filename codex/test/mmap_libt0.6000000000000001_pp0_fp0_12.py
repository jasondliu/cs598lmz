import mmap
import os

import colorama

from . import shared


class MMapFile(object):
    def __init__(self, fd, length, offset=0, access=mmap.ACCESS_WRITE):
        self.file = mmap.mmap(fd, length, access=access, offset=offset)
        self.length = length
        self.offset = offset

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        self.file.close()


class BinaryFile(object):

    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.mmap = None

    def open(self, mode='r'):
        self.file = open(self.filename, mode)
