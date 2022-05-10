import lzma
# Test LZMADecompressor

def test_LZMADecompressor():
    c = lzma.LZMADecompressor()
    assert c.decompress(b'BZh91AY&SY') == b'hello'
    assert c.unused_data == b''
    assert c.eof
    assert c.decompress(b'BZh91AY&SY') == b'hello'
    assert c.unused_data == b'BZh91AY&SY'
    assert c.eof
    assert c.decompress(b'BZh91AY&SY', max_length=5) == b'hello'
    assert c.unused_data == b'BZh91AY&SY'
    assert c.eof
    assert c.decompress(b'BZh91AY&SY', max_length=4) == b'hell'
    assert c.unused_data == b'BZh91AY&SY'
    assert not c.eof
    assert c.decompress(b'o') == b'o'
