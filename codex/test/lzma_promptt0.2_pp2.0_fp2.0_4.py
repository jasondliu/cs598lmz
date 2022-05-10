import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    with open('testdata/lzma_compressed.txt', 'rb') as f:
        data = f.read()
    d = lzma.LZMADecompressor()
    assert d.decompress(data) == b'This is a test.\n'
    assert d.unused_data == b''
    assert d.eof
    assert d.decompress(b'blah') == b''
    assert d.unused_data == b'blah'
    assert not d.eof
    assert d.decompress(b'blah', max_length=1) == b'b'
    assert d.unused_data == b'lah'
    assert not d.eof
    assert d.decompress(b'blah', max_length=1) == b'l'
    assert d.unused_data == b'ah'
    assert not d.eof
