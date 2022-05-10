import lzma
# Test LZMADecompressor with a short input.
with lzma.LZMADecompressor() as d:
    assert d.decompress(b'x\x9c+I\xce\xcfML\xc8\xcc\xc1\t\x00\x0b\x04]\x06\xf0') == b'1234567890'

# Test LZMADecompressor with a long input.
data = lzma.compress(b'1234567890' * 1000)
with lzma.LZMADecompressor() as d:
    assert d.decompress(data) == b'1234567890' * 1000

# Test LZMADecompressor with max_length specified.
with lzma.LZMADecompressor(format=lzma.FORMAT_XZ) as d:
    assert d.decompress(data, max_length=100) == b'1234567890' * 10

# Test LZMADecompressor with a truncated input.
with lzma.LZ
