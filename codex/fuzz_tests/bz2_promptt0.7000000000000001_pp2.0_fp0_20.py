import bz2
# Test BZ2Decompressor
class TestBZ2Decompressor(unittest.TestCase):
    def test_decompressor_object(self):
        decompressor = bz2.BZ2Decompressor()
        self.assertEqual(decompressor.decompress(b"x\x9c+\x80\x00\x00\x00\x00\x00\x00\x01\x02\x00"), b"")
        self.assertEqual(decompressor.unused_data, b"")
        self.assertEqual(decompressor.decompress(b"\x03\x00\x00\x00\x00\x00\x00\x00\x04"), b"")
        self.assertEqual(decompressor.unused_data, b"\x03\x00\x00\x00\x00\x00\x00\x00\x04")
        self.assertEqual(decompressor.decompress(b"\x00"), b"foo")
        self.assertEqual(decomp
