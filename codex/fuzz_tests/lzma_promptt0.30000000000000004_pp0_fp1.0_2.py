import lzma
# Test LZMADecompressor

# Test basic functionality

d = lzma.LZMADecompressor()
assert d.unused_data == b""
assert d.eof is False

# Test decompression

data = lzma.compress(b"test")
assert d.decompress(data) == b"test"
assert d.unused_data == b""
assert d.eof is True

# Test that decompression fails after eof

with pytest.raises(EOFError):
    d.decompress(b"test")

# Test that decompression fails after eof even if unused_data is set

d = lzma.LZMADecompressor()
d.decompress(data, max_length=4)
assert d.unused_data == b"test"
assert d.eof is True

with pytest.raises(EOFError):
    d.decompress(b"test")

# Test that decompression fails after eof even if unused_data is set
# and max_length is used

d
