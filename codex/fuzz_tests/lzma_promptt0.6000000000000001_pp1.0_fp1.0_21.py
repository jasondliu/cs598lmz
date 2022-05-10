import lzma
# Test LZMADecompressor

def test_decompressor():
    # LZMADecompressor is a stream
    d = lzma.LZMADecompressor()
    big = b'\x00' * 100000
    small = d.decompress(big)
    assert len(small) == 100000
    assert small == b'\x00' * 100000
    # LZMADecompressor has some methods
    d = lzma.LZMADecompressor()
    d.decompress(b'\x00')
    assert d.unused_data == b''
    assert d.eof
    d = lzma.LZMADecompressor()
    d.decompress(b'\x00', max_length=1)
    assert d.unused_data == b'\x00'
    assert not d.eof
    # LZMADecompressor.flush()
    d = lzma.LZMADecompressor()
    d.decompress(b'\x00')
    assert d
