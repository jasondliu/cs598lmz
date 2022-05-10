import lzma
# Test LZMADecompressor

compressor = lzma.LZMACompressor(lzma.FORMAT_ALONE)
decompressor = lzma.LZMADecompressor(lzma.FORMAT_ALONE)

data = b'data to compress'
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressed = decompressor.decompress(compressed)
assert decompressed == data

decompressed = decompressor.decompress(b'')
assert decompressed == b''

# Test that LZMADecompressor.decompress() raises EOFError if given incomplete
# data.
decompressor = lzma.LZMADecompressor(lzma.FORMAT_ALONE)

data = b'data to compress'
compressed = compressor.compress(data)
compressed = compressed[:-1]

try:
    decompressor.decompress(compressed)
except EOFError:
    pass
else:
    assert False, 'EOFError not raised'

# Test L
