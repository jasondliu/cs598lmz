import lzma
# Test LZMADecompressor

def test_lzma_decompressor_read():
    # Test that LZMADecompressor.read() works correctly
    data = b'\x00' * 100 + b'foo'
    cdata = lzma.compress(data)
    d = lzma.LZMADecompressor()
    assert d.read(10) == b''
    assert d.read(10) == b''
    assert d.unconsumed_tail == b''
    d.decompress(cdata[:10])
    assert d.unconsumed_tail == cdata[10:10]
    assert d.read(10) == b''
    assert d.read(10) == b''
    assert d.unconsumed_tail == cdata[10:10]
    d.decompress(cdata[10:20])
    assert d.unconsumed_tail == cdata[20:10]
    assert d.read(10) == b''
    assert d.read(10) == b''
    assert d.unconsumed_
