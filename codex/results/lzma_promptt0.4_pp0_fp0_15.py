import lzma
# Test LZMADecompressor

def test_LZMADecompressor():
    c = lzma.LZMADecompressor()
    data = b"foo"
    c.decompress(data)
    c.flush()
    c.decompress(data)
    c.flush()
    c.decompress(data)
    c.flush()
    c.decompress(data)
    c.flush()
    c.decompress(data)
    c.flush()
    c.decompress(data)
    c.flush()
    c.decompress(data)
    c.flush()
    c.decompress(data)
    c.flush()
    c.decompress(data)
    c.flush()
    c.decompress(data)
    c.flush()
    c.decompress(data)
    c.flush()
    c.decompress(data)
    c.flush()
    c.decompress(data)
    c.flush()
    c.decompress(data)

