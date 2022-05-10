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
codecs.encode('abc', 'hex')

import zlib
zlib.compress(b'abc')

import _codecs
_codecs.encode('abc', 'hex')


# test case for issue #19138
import _imp
_imp.create_dynamic('_dummy', '', '_dummy')

# test case for issue #17056
import sys
sys.implementation.name
sys.implementation.cache_tag

# test case for issue #17056
import _frozen_importlib
_frozen_importlib.is_frozen
