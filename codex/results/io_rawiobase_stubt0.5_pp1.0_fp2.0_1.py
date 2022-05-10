import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b):
        self.file.write(b)
        return len(b)
    def seek(self, offset, whence=0):
        self.file.seek(offset, whence)
    def close(self):
        self.file.close()

def file(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
    if closefd:
        return File(file)
    else:
        return file

import time
def sleep(secs):
    time.sleep(secs)

import sys
def exit(arg):
    sys.exit(arg)

import random
def randint(a, b):
    return random.randint(a, b)

def randrange(start, stop=None, step=1):
    return random.randrange(start, stop,
