import lzma
# Test LZMADecompressor.
def test_lzmadecompressor():
    compress = lzma.LZMACompressor()
    uncompress = lzma.LZMADecompressor()
    cdata = compress.compress(data * 10)
    cdata += compress.flush()
    ucdata = uncompress.decompress(cdata)
    assert ucdata == data * 10, ucdata
