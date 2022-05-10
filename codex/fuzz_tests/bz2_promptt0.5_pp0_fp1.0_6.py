import bz2
# Test BZ2Decompressor

class TestBZ2Decompressor(unittest.TestCase):

    def test_decompressor(self):
        # check that the decompressor can be used repeatedly
        # to decompress the same data
        data = bz2.compress(b"this is the first time that I compress this.")
        d = bz2.BZ2Decompressor()
        for i in range(2):
            self.assertEqual(d.decompress(data), b"this is the first time that I compress this.")
            self.assertEqual(d.unused_data, b"")

    def test_partial(self):
        # check that the decompressor can be used repeatedly
        # to decompress the same data
        data = bz2.compress(b"this is the first time that I compress this.")
        d = bz2.BZ2Decompressor()
        self.assertEqual(d.decompress(data[:10]), b"")
        self.assertEqual(d.decompress(data[10:20]), b"")
