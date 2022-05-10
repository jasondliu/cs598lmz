import lzma
# Test LZMADecompressor with a file containing a single empty LZMA stream.
with lzma.open(BytesIO(b'\x5d\x00\x00\xff\xff'), "r") as f:
    assert f.read() == b''

# Test LZMADecompressor with a file containing a single empty LZMA stream
# with an empty filter chain.
with lzma.open(BytesIO(b'\x5d\x00\x00\x00\x00'), "r") as f:
    assert f.read() == b''

# Test LZMADecompressor with a file containing a single empty LZMA stream
# with an empty filter chain and a non-zero uncompressed size.
with lzma.open(BytesIO(b'\x5d\x00\x00\x00\x00\x00\x00\x00\x01'), "r") as f:
    assert f.read() == b''

# Test LZMADecompressor with a file containing a single empty LZMA stream
# with an empty filter
