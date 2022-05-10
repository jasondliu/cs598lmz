import lzma
# Test LZMADecompressor.eof

def test_eof():
    lz = lzma.LZMADecompressor()
    assert not lz.eof
    lz.decompress(b'\x00')
    assert lz.eof
    assert lz.decompress(b'') == b''
    assert lz.eof
    assert lz.decompress(b'\x00') == b''
    assert lz.eof
    lz.decompress(lzma.compress(b'a'))
    assert lz.eof

# Test LZMADecompressor.decompress() boundary conditions
# and error detection.

def test_decompress():
    lz = lzma.LZMADecompressor()
    assert lz.decompress(b'') == b''
    assert lz.decompress(b'\x00') == b''
    assert lz.decompress(b'\x01\x00\x00') == b''
    assert lz.
