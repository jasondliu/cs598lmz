import lzma
# Test LZMADecompressor with a stream that ends with an incomplete chunk.
# This should raise an EOFError.

data = lzma.compress(b"foo")
data = data[:-1]

decompressor = lzma.LZMADecompressor()
with pytest.raises(EOFError):
    decompressor.decompress(data)
# Test LZMADecompressor with a stream that ends with an incomplete chunk,
# but with a valid end of stream marker.

data = lzma.compress(b"foo")
data = data[:-1]
data += b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00"

decompressor = lzma.LZMADecompressor()
with pytest.raises(EOFError):
    decompressor.decompress(data)
# Test LZMADecompressor with a stream that ends with an incomplete chunk,
# but with a valid end of stream marker.

data = lzma.compress
