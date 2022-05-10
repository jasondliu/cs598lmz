import mmap
import os
import sys
import time

class Mmap:
    def __init__(self, fname):
        self.fname = fname
        self.f = None
        self.m = None
        self.size = 0

    def open(self):
        self.f = open(self.fname, "r+b")
        self.size = os.path.getsize(self.fname)
        self.m = mmap.mmap(self.f.fileno(), self.size)
        return self

    def close(self):
        self.m.close()
        self.f.close()
        return self

    def __enter__(self):
        return self.open()

    def __exit__(self, type, value, traceback):
        return self.close()

    def __getitem__(self, key):
        return self.m[key]

    def __setitem__(self, key, value):
        self.m[key] = value
        return self

def main():
    fname = sys.arg
