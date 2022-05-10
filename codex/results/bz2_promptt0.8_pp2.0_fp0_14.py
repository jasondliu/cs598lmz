import bz2
# Test BZ2Decompressor.__iter__

ZERO_BYTE = b''

class TestIter(unittest.TestCase):

    def test_simple(self):
        # Test that calling the iterator's next() method repeatedly
        # returns the compressed data one chunk at a time
        compressor = bz2.BZ2Compressor()
        chunks = []
        for chunk in compressor:
            chunks.append(chunk)
        self.assertEqual(b"".join(chunks), ZERO_BYTE)

    def test_cornercases(self):
        # Test that passing data through a BZ2Decompressor object
        # in small chunks (fewer than 100 bytes) works correctly.
        for chunk_size in range(1, 100):
            compressor = bz2.BZ2Compressor()
            chunks = []
            for i in range(0, len(ZERO_BYTE), chunk_size):
                chunks.append(compressor.compress(ZERO_BYTE[i:i+chunk_size]))
                if len(chunks[-1]) == 0:
