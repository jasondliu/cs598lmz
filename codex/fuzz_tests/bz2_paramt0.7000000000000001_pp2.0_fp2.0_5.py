from bz2 import BZ2Decompressor
BZ2Decompressor.__module__ = 'bz2'

from . import get_data

class TestBZ2(unittest.TestCase):
    def test_read1(self):
        data = get_data('test1.bz2')
        x = BZ2Decompressor()
        self.assertEqual(x.decompress(data), b'BZh91AY&SY\x94\x8e\x0e\x00\x00\x00\x81\x04$|\x0e\xc9\xc8,\x00!\x0e\x98?')
        self.assertEqual(x.flush(), b'M\xf5\x00\xfa\x00\xff\x00\xfe\x00\xf7\x00\xfc\x00\xfd\x00\xf3\x00\xfa\x00\xfb\x00\xf2\x00\xf9\x00\xfc\x00\xfb\x00\xf5\x00\xf8\x00
