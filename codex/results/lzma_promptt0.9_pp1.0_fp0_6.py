import lzma
# Test LZMADecompressor constructor
try:
    lzma.LZMADecompressor()
except RuntimeError:
    # lzma module segfaults
    import unittest
    raise unittest.SkipTest("lzma module segfaults")

import bz2
try:
    bz2.open(TESTFN, 'w').close()
except OSError:
    import unittest
    raise unittest.SkipTest("bzip2 is not supported")

import zlib
# open() should not crash even with negative wbits
with zlib.open(TESTFN, 'w') as f:
    f.write('test')

from importlib import reload
import datetime
import _strptime
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    reload(_strptime)
    # see #3746
    datetime.datetime.strptime('', '')

# https://bugs.python.org/issue32923
with open(TESTFN, 'w') as f:
    f.write('
