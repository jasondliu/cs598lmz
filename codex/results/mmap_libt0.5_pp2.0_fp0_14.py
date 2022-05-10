import mmap
import os
import struct
import sys

import lib.util as util

class File:
    def __init__(self, filename, mode = 'rb'):
        self.filename = filename
        self.mode = mode
        self.file = open(filename, mode)
        self.mmap = mmap.mmap(self.file.fileno(), 0, access = mmap.ACCESS_READ)
        self.size = os.path.getsize(filename)
        self.current = 0

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.file.close()
        self.mmap.close()

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.size:
            raise StopIteration
        else:
            start = self.current
            end = self.current = self.current + 1
            return self.mmap[start:end]

    def read(self, bytes):
        start = self.
