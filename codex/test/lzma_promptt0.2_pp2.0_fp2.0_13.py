import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test basic functionality
    d = lzma.LZMADecompressor()
    e = lzma.LZMACompressor()
    for func in ('decompress', 'flush'):
        assert not hasattr(d, func)
    for i in range(500):
        s = e.compress(bytes(i))
        if s:
            t = d.decompress(s)
            assert t == bytes(i)
    t = d.flush()
    assert t == b''
    # Test multiple decompress() calls
    d = lzma.LZMADecompressor()
    e = lzma.LZMACompressor()
    for i in range(500):
        s = e.compress(bytes(i))
        if s:
            t = d.decompress(s)
            assert t == bytes(i)
    t = d.flush()
    assert t == b''
    # Test buffer size
    d = lzma.LZM
