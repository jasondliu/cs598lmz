import lzma
# Test LZMADecompressor.read()

def test_read():
    data = b'\x00' * 100 + b'\xFF' * 100
    compressed = lzma.compress(data)
    assert lzma.decompress(compressed) == data

    d = lzma.LZMADecompressor()
    assert d.decompress(compressed) == data

    d = lzma.LZMADecompressor()
    d.decompress(compressed[:16])
    assert d.unused_data == compressed[:16]
    d.decompress(compressed[16:])
    assert d.unused_data == b''

    d = lzma.LZMADecompressor()
    assert d.decompress(compressed[:16], max_length=200) == b''
    assert d.unused_data == compressed[:16]
    assert d.decompress(compressed[16:], max_length=200) == data
    assert d.unused_data == b''

    d = l
