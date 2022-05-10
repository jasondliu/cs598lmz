import lzma
# Test LZMADecompressor

def test_decompressor_init():
    lzc = lzma.LZMADecompressor()
    assert lzc
    assert lzc.eof is False
    assert lzc.unused_data == b''
    assert lzc.unconsumed_tail == b''
    lzc = lzma.LZMADecompressor(format=lzma.FORMAT_AUTO)
    assert lzc.format == lzma.FORMAT_XZ
    lzc = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
    assert lzc.format == lzma.FORMAT_XZ
    lzc = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
    assert lzc.format == lzma.FORMAT_ALONE
    lzc = lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
    assert lzc.format
