import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    data = b"\x00" * 1000000
    cdata = lzma.compress(data)
    d = lzma.LZMADecompressor()
    assert d.decompress(cdata) == data
    assert d.unused_data == b""
    assert d.eof == True
    assert d.decompress(b"garbage") == b""
    assert d.unused_data == b"garbage"
    assert d.eof == False
    assert d.decompress(b"") == b""
    assert d.unused_data == b"garbage"
    assert d.eof == False
    assert d.decompress(b"moregarbage") == b""
    assert d.unused_data == b"garbagemoregarbage"
    assert d.eof == False
    assert d.decompress(b"") == b""
    assert d.unused_data == b"garbagemoregarbage"
    assert d.
