import lzma
# Test LZMADecompressor to make sure we have one.
# This is just a smoke test; this is not a functional test of the
# LZMA library.
with lzma.LZMADecompressor() as d:
    pass
# Test LZMACompressor to make sure we have one.
# This is just a smoke test; this is not a functional test of the
# LZMA library.
with lzma.LZMACompressor() as c:
    pass
# A simple test that the LZMADecompressor object is iterable.
with lzma.LZMADecompressor() as d:
    for chunk in d:
        pass
# A simple test that the LZMACompressor object is iterable.
with lzma.LZMACompressor() as c:
    for chunk in c:
        pass
# A simple test that the LZMADecompressor object is callable.
with lzma.LZMADecompressor() as d:
    d()
# A simple test that the LZMACompressor object is callable.
with l
