import bz2
# Test BZ2Decompressor

def test_bz2decompressor():
    c = bz2.BZ2Decompressor()
    assert c.decompress(b'BZh91AY&SY') == b'hello'
    assert c.unused_data == b''
    c = bz2.BZ2Decompressor()
    assert c.decompress(b'BZh91AY&SYh') == b'hello'
    assert c.unused_data == b'h'
    c = bz2.BZ2Decompressor()
    assert c.decompress(b'BZh91AY&SYhI') == b'hello'
    assert c.unused_data == b'hI'
    c = bz2.BZ2Decompressor()
    assert c.decompress(b'BZh91AY&SYhIh') == b'hello'
    assert c.unused_data == b'hIh'
    c = bz2.BZ2Decompressor()
