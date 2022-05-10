import lzma
# Test LZMADecompressor compatibility with bz2
# See https://bugs.python.org/issue42304
def test_lzma_bz2():
    b = bz2.compress(b'hello')
    d = lzma.LZMADecompressor()
    assert d.decompress(b) == b'hello'
    with pytest.raises(lzma.LZMAError):
        d.decompress(b[:1])
    with pytest.raises(lzma.LZMAError):
        d.decompress(b'\x00')
    with pytest.raises(lzma.LZMAError):
        d.decompress(b'\x00' * 4)

def test_lzma_memoryview():
    b = bz2.compress(b'hello')
    d = lzma.LZMADecompressor()
    assert d.decompress(memoryview(b)) == b'hello'

# Test pyexpat compatibility with bz2
# See https://bugs
