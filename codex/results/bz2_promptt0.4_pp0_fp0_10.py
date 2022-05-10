import bz2
# Test BZ2Decompressor with a simple file

class TestBZ2Decompressor(unittest.TestCase):
    def test_decompress(self):
        with bz2.open(TESTFN, 'rb') as f:
            d = bz2.BZ2Decompressor()
            data = f.read(100)
            self.assertEqual(d.decompress(data),
                             b'BZh91AY&SY\xd8\xdd\xd5\x0b\x00\x00\x00\x80\x00\x10@\x00 \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')
            data = f.read(100)
            self.assertEqual(d.decompress(data),
                             b'\x7f\xff\x7f\xfd\xcb\xcf\x04\x00\x1b\x00\x00\x00\x04\x00\x1c\x00\
