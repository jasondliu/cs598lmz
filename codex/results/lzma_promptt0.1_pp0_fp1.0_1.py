import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test basic functionality
    d = lzma.LZMADecompressor()
    assert d.decompress(b"") == b""
    assert d.unused_data == b""
    assert d.eof == False
    assert d.decompress(b"asdf") == b"asdf"
    assert d.unused_data == b""
    assert d.eof == False
    assert d.decompress(b"") == b""
    assert d.unused_data == b""
    assert d.eof == False
    assert d.decompress(b"foo") == b"foo"
    assert d.unused_data == b""
    assert d.eof == False
    assert d.decompress(b"", True) == b""
    assert d.unused_data == b""
    assert d.eof == True
    raises(EOFError, d.decompress, b"")
    assert d.unused_data == b""
   
