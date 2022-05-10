import mmap
import os
import sys

class MMapFile:
    def __init__(self, filename, mode='r'):
        self.mode = mode
        self.filename = filename
        self.file = open(self.filename, self.mode)
        self.mmap = mmap.mmap(self.file.fileno(), 0, access=mmap.ACCESS_READ)

    def __del__(self):
        self.mmap.close()
        self.file.close()

    def read(self, length):
        return self.mmap.read(length)

class MMapFileWriter:
    def __init__(self, filename, mode='w+'):
        self.mode = mode
        self.filename = filename
        self.file = open(self.filename, self.mode)
        self.mmap = mmap.mmap(self.file.fileno(), 0)

    def __del__(self):
        self.mmap.close()
        self.file.close()

    def write(self, data):
        self.mm
