import lzma
# Test LZMADecompressor

data = b"".join(bytes([x % 256]) for x in range(256)) * 256

def test_LZMADecompressor():
    c = lzma.LZMADecompressor()
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

