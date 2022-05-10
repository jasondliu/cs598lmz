import lzma
# Test LZMADecompressor.decompress()

def test_decompress():
    # Test that decompressing a stream compressed with LZMA.compress()
    # gives the original data.
    data = b"1234567890" * 1000
    cdata = lzma.compress(data)
    d = lzma.LZMADecompressor()
    ddata = d.decompress(cdata)
    assert ddata == data

def test_decompress_unused_data():
    # Test that unused_data is set correctly.
    data = b"1234567890" * 1000
    cdata = lzma.compress(data)
    d = lzma.LZMADecompressor()
    ddata = d.decompress(cdata[:-5])
    assert d.unused_data == cdata[-5:]
    ddata = d.decompress(cdata[-5:])
    assert d.unused_data == b""
    assert ddata == data[-5:]

def test_decompress_
