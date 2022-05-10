import mmap
import os
import re

__author__ = 'Tramy'


class MmapHack:
    def __init__(self, filename, mode='r'):
    # def __init__(self, filename):
        self.fp = open(filename, mode)
        self.byte_size = os.path.getsize(filename)
        self.map = mmap.mmap(self.fp.fileno(), self.byte_size)

    def __getitem__(self, index):
        return self.map.__getitem__(index)

    def __del__(self):
        self.map.close()
        self.fp.close()


