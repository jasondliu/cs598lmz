from bz2 import BZ2Decompressor
BZ2Decompressor.flush = lambda self: self.decompress('')

class TestCompressor(TestCase):

    def test_compress(self):
        # compress() returns more data after each call
        eq = self.assertEqual
        c = BZ2Compressor()
        eq(c.compress(b("foo")), b("BZh"))
        eq(c.compress(b("bar")), b("1AY&SY"))
        eq(c.compress(b("baz")), b(""))
        eq(c.flush(), b("Az\x01"))
        # compress() accepts bytes or bytearray
        c = BZ2Compressor()
        eq(c.compress(b("foo")), b("BZh"))
        eq(c.compress(bytearray(b("bar"))), b("1AY&SY"))
        eq(c.compress(bytearray(b("baz"))), b(""))
        eq(c.flush(), b("Az\x01"))
        # compress() accepts memoryviews
        c =
