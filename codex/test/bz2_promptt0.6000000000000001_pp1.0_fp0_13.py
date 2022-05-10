import bz2
# Test BZ2Decompressor

def test_bz2decompressor_new_methods():
    # test new methods added by issue #1706
    d = bz2.BZ2Decompressor()
    assert d.unused_data == b''
    d.decompress(b'BZh91AY&SY')
    assert d.unused_data == b'BZh91AY&SY'
    d.decompress(b'BZh91AY&SY')
    d.unused_data += b'BZh91AY&SY'
    d.decompress(b'BZh91AY&SY')
    assert d.unused_data == b''

def test_bz2decompressor_with_read():
    # test read() method added by issue #1706
    d = bz2.BZ2Decompressor()
    data = d.decompress(b'BZh91AY&SY')
    assert d.unused_data == b'BZh91AY&SY'
    data += d.read()
