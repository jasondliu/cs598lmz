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
re.V1
re.V2
re.V0
re.IGNORECASE | re.VERBOSE
# Test new methods
re.fullmatch('ab', 'ab')
# Test fullmatch()
re.match('ab+', 'abbbbbbb', pos=2)
re.match('ab+', 'abbbbbbb', endpos=3)
# Test pos and endpos arguments
re.purge()

import selectors
# Test EXTENDED fileobj support

