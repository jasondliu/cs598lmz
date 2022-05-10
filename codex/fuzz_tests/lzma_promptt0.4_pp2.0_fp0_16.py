import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    data = b"Hello world!"
    cdata = lzma.compress(data)
    d = lzma.LZMADecompressor()
    ddata = d.decompress(cdata)
    assert ddata == data
    assert d.unused_data == b""
    ddata = d.decompress(b"garbage")
    assert ddata == b""
    assert d.unused_data == b"garbage"
    assert d.eof is False
    ddata = d.decompress(b"", True)
    assert ddata == b""
    assert d.unused_data == b""
    assert d.eof is True
    d.decompress(b"")
    assert d.eof is True
    d.decompress(b"", True)
    assert d.eof is True
    #
    d = lzma.LZMADecompressor()
    ddata = d.decompress(b"garbage", True
