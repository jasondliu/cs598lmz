import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
data = b'.'
while True:
    # Feed data in piece by piece, until you have
    # all of the original data
    buf = decompressor.decompress(data)
    if buf:
        print(buf)
    if decompressor.eof:
        break
    data = b'.'

# Finish up
buf = decompressor.flush()
print(buf)

# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Feed data to the compressor
data = b'This is the data to compress'
compressed = compressor.compress(data)
print(compressed)

# Finish up
compressed += compressor.flush()
print(compressed)

# Test LZMAFile

# Create a compressor object
compressor = lzma.LZMACompressor()

# Write compressed data to a file
with open
