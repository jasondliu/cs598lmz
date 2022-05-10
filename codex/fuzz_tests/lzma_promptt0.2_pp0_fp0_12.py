import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test that LZMADecompressor can decompress a file created by
    # xz -9.
    with open('testdata/lzma.xz', 'rb') as f:
        compressed = f.read()
    with open('testdata/lzma.txt', 'rb') as f:
        uncompressed = f.read()
    d = lzma.LZMADecompressor()
    assert d.decompress(compressed) == uncompressed
    assert d.unused_data == b''
    assert d.eof is True
    assert d.decompress(b'blah') == b''
    assert d.unused_data == b'blah'
    assert d.eof is False
    assert d.decompress(b'blah', max_length=2) == b''
    assert d.unused_data == b'blah'
    assert d.eof is False
    assert d.decompress(b'blah', max_length=
