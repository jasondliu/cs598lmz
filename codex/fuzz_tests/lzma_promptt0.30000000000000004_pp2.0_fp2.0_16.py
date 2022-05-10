import lzma
# Test LZMADecompressor.decompress()

def test_decompress_1():
    data = b'\x00' * 1024
    compressed = lzma.compress(data)
    d = lzma.LZMADecompressor()
    assert d.decompress(compressed) == data

def test_decompress_2():
    data = b'\x00' * 1024
    compressed = lzma.compress(data)
    d = lzma.LZMADecompressor()
    assert d.decompress(compressed, max_length=512) == data[:512]

def test_decompress_3():
    data = b'\x00' * 1024
    compressed = lzma.compress(data)
    d = lzma.LZMADecompressor()
    assert d.decompress(compressed, max_length=512) == data[:512]
    assert d.decompress(b'', max_length=512) == data[512:1024]

def test_decompress
