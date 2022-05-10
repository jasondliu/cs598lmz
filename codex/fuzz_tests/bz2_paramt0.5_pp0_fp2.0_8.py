from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = decompress

from . import *

class TestDecompressor(unittest.TestCase):
    def test_decompress(self):
        self.assertEqual(decompress(b'BZh91AY&SY\xd8N\x18\x00\x01>_\x80\x00\x10@\x02\xff\xff\x89\xe0\x1dH\x01\xdf\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00;'), b'hello')

    def test_decompress_bad_data(self):
        self.assertRaises(ValueError, decompress, b'BZh91AY&SY\xd8N\x18\x00\x01>_\x80\x00\x10@\x02\xff\xff\x89\xe0\x1dH\x01\xdf\xff\xff\xff\xff\xff\xff\xff\xff\xff
