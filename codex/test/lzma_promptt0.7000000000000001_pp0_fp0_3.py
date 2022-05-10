import lzma
# Test LZMADecompressor.read()

decompressor = lzma.LZMADecompressor()

# Feed the decompressor with bytes until it needs more input
# and the EOF flag is set.
data = b''
