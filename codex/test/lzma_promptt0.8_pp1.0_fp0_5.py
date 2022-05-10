import lzma
# Test LZMADecompressor
del lzma

import os
# Test seek() and tell()
os.SEEK_HOLE

import platform
# Test whether sys.version_info >= (3, 8)
platform.python_implementation()

import random
# Test __all__
random.__all__
# Test pickle support
random.Random().__reduce__()
# Test random.choices()
random.choices(population=[1, 2], weights=[0.5, 0.5], k=10)

import re
# Test new flags
re.DEBUG
re.ASCII
re.LOCALE
