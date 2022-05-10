import bz2
# Test BZ2Decompressor.decompress()

def decompress(data):
    d = bz2.BZ2Decompressor()
    try:
        return d.decompress(data)
    except IOError:
        return d.decompress(data + b'\0')

def test_decompress():
    data = b'BZh91AY&SY\xd8\xcb\x97\x80 \x00\x00\x01\x01\x80@\x02 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    assert decompress(data) == b'hello'
    assert decompress(data * 100) == b'hello' * 100
    assert decompress(data * 100 + b'\0') == b'hello' * 100
    assert decompress(data * 100 + b'\xff') == b'hello' * 100
    assert decompress(data * 100 + b'\xff\0') == b'hello' * 100
    assert decomp
