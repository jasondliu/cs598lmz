import lzma
# Test LZMADecompressor

try:
    lzma.LZMADecompressor
except AttributeError:
    if sys.version_info[0:2] == (3, 5):
        import unittest
        raise unittest.SkipTest("LZMADecompressor is not available on Python 3.5.")
    else:
        raise

data = open(__file__, "rb").read()
cdata = lzma.compress(data)
decomp = lzma.LZMADecompressor()
assert len(decomp.decompress(cdata)) >= len(data)
