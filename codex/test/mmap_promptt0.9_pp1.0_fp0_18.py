import mmap
# Test mmap.mmap.resize()
from mmap import *
from test import test_support
from random import random, randint
from os import unlink, system, name
import cStringIO
from os.path import getsize

import pdb
import sys

# helper function
def copyfileobj(fsrc, fdst, length=16*1024):
    """copy data from file-like object fsrc to file-like object fdst"""
    while True:
        buf = fsrc.read(length)
        if not buf:
            break
        fdst.write(buf)

# Return the size of a file (of name filename).
def getsize(filename):
    """Return the size of a file, reported by os.stat()."""
    import os
    return os.stat(filename).st_size

FILESIZE = 10000
FILE2SIZE = FILESIZE*10

def create_file(name, size, seed=None):
    """Create a file of given name and size."""
    f = open(name, 'w')
