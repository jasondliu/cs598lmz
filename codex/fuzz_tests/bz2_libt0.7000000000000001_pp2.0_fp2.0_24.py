import bz2
bz2_compress = bz2.compress
bz2_decompress = bz2.decompress

# test set
try:
    from test_set_for_xrange import *
except ImportError:
    from sets import Set as set
    from __builtin__ import xrange as range

import unittest
from nose.plugins.skip import SkipTest

def _skip_if_no_lzma():
    try:
        import lzma
    except ImportError:
        raise SkipTest('No lzma module')

class TestCompressDecompress(unittest.TestCase):

    def test_decompress(self):
        self.assertEqual(zlib_decompress(zlib_compress('abc')), 'abc')
        self.assertEqual(zlib_decompress(zlib_compress('abc', 6)), 'abc')

        self.assertEqual(gzip_decompress(gzip_compress('abc')), 'abc')
        self.assertEqual(gzip_decompress(
