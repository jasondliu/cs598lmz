import lzma
# Test LZMADecompressor

# Test that the decompressor object can be used to decompress data after
# the end-of-stream marker has been found.

decompressor = lzma.LZMADecompressor()

data = b"x" * 100 + lzma.LZMA_EOS
assert decompressor.decompress(data) == b"x" * 100
assert decompressor.decompress(b"y") == b"y"
# Test LZMADecompressor.decompress()

# Test that the decompressor object can be used to decompress data after
# the end-of-stream marker has been found.

decompressor = lzma.LZMADecompressor()

data = b"x" * 100 + lzma.LZMA_EOS
assert decompressor.decompress(data) == b"x" * 100
assert decompressor.decompress(b"y") == b"y"
# Test LZMADecompressor.flush()

# Test that the decompressor object can be used to decompress data after

