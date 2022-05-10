import lzma
# Test LZMADecompressor

def test_LZMADecompressor_1():
    c = lzma.LZMADecompressor()
    empty = b''
    assert c.unused_data == empty
    assert c.decompress(empty) == empty
    assert c.unused_data == empty
    assert c.decompress(b'X') == empty
    assert c.unused_data == b'X'
    assert c.decompress(empty, max_length=0) == empty
    assert c.unused_data == b'X'
    assert c.decompress(b'12345', max_length=5) == b'12345'
    assert c.unused_data == empty
    assert c.decompress(b'12345', max_length=4) == b'1234'
    assert c.unused_data == b'5'
    assert c.decompress(b'67890', max_length=10) == b'567890'
    assert c.unused_data == empty

def test_LZ
