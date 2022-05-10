import lzma
# Test LZMADecompressor with a stream that ends with an incomplete chunk.
# This should raise an EOFError.

data = lzma.compress(b"foo")
data = data[:-1]

decompressor = lzma.LZMADecompressor()
