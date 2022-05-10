import bz2
# Test BZ2Decompressor.

# This is a guess at the minimum amount of data needed to trigger
# the bug.  If it's wrong, the test will fail with a short read
# exception.

# This test is skipped if the bz2 module wasn't compiled with the
# BZ2_DECOMPRESS_SMALL feature.

try:
    bz2.BZ2Decompressor.decompress("")
except NotImplementedError:
    raise unittest.SkipTest("bz2.BZ2Decompressor.decompress() not implemented")

class DecompressTest(unittest.TestCase):
    def test_decompress(self):
        d = bz2.BZ2Decompressor()
        self.assertEqual(d.decompress(""), "")
        self.assertEqual(d.decompress("BZh9"), "")
        self.assertEqual(d.decompress("BZh9\x00"), "")
        self.assertEqual(d.decompress("BZh9\x00\x
