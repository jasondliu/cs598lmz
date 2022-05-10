import lzma
lzma.LZMACompressor()

import math
math.acos(0.123)

import os
os.remove('spam')

try:
    import spam
except ImportError:
    print('ImportError')

import tempfile
tempfile.TemporaryFile()

import time
time.asctime()

import tracemalloc # disable
tracemalloc.start()
