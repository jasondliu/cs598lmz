import lzma
# Test LZMADecompressor objects

class BaseTest:
    def test_non_readable_counters(self):
        # "Those counters that cannot be read in the current state (either
        # because they are meaningless in the current state or because no
        # meaningful value has been set, clear or returned yet) will raise
        # an AttributeError."
        decomp = lzma.LZMADecompressor()
        for counter in (decomp._bad_bytes, decomp._avail_in, decomp._buffer):
            self.assertRaises(AttributeError, getattr, decomp, counter)

        self.assertEqual(decomp._total_in, 0)
        self.assertEqual(decomp._used_filters, [])


class StreamTest(BaseTest):
    # Test basic compression and decompression

    def test_basic(self):
        cdata = b'Hello, world'
        self.assertEqual(lzma.decompress(lzma.compress(cdata)), cdata)

    def test_buffer(self):
        decomp = lzma.LZMAD
