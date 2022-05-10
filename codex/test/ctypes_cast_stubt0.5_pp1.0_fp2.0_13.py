import ctypes
ctypes.cast(0, ctypes.py_object)

import sys
sys.getrefcount(1)

import time
time.time()

import random
random.random()

import os
os.getpid()

import array
array.array('i', [0, 1, 2, 3])

import itertools
for _ in itertools.repeat(None, 4): pass

import struct
struct.pack('i', 12345)

import codecs
