import bz2
# Test BZ2Decompressor.decompress()

class TestBZ2Decompressor_Decompress(unittest.TestCase):
    def test_multiple_calls(self):
        data = bz2.decompress(COMPRESSED_TEXT)
        d = bz2.BZ2Decompressor()
        self.assertEqual([d.decompress(COMPRESSED_TEXT[:5]),
                          d.decompress(COMPRESSED_TEXT[5:10]),
                          d.decompress(COMPRESSED_TEXT[10:15]),
                          d.decompress(COMPRESSED_TEXT[15:])],
                         [data[:5], data[5:10], data[10:15], data[15:]])
        # Decompress some more, to check the internal state
        self.assertEqual([d.decompress(COMPRESSED_TEXT[:5]),
                          d.decompress(COMPRESSED_TEXT[5:10]),
                          d.decompress(COMPRESSED_TEXT[10:15]),
                         
