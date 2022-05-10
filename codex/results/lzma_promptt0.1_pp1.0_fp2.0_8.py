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
    data = input()

# Flush any remaining data
buf = decompressor.flush()
print(buf)

# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Compress some data
data = b'This is the original text.'
buf = compressor.compress(data)
print(buf)

# Flush the compressor to get any remaining data
buf = compressor.flush()
print(buf)

# Test LZMAFile

# Create a compressor object
compressor = lzma.LZMACompressor()

# Compress some data
data
