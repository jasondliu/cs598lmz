import lzma
# Test LZMADecompressor with bad data
def test_lzma_decompressor_bad_data():
    dc = lzma.LZMADecompressor()
    dc.decompress(b'bad data')
    raises(lzma.LZMAError, dc.decompress, b'')
    raises(lzma.LZMAError, dc.decompress, b'bad data')
    raises(lzma.LZMAError, dc.flush)
