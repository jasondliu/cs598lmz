import lzma
# Test LZMADecompressor.__repr__
class Test_LZMADecompressor_repr(unittest.TestCase):
    def test_repr(self):
        d = lzma.LZMADecompressor()
        # Just test that it doesn't crash
        d.__repr__()
        d.flush(1)
        d.__repr__()
        d = lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
        d.__repr__()
        d.flush(1)
        d.__repr__()
        d = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
        d.__repr__()
        d.flush(1)
        d.__repr__()
        d = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
        d.__repr__()
        d.flush(1)
        d.__repr__()


def test_main
