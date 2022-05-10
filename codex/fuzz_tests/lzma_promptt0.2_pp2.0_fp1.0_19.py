import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
data = b'.'
while True:
    # Feed data in piece by piece, until you get EOF
    buf = decompressor.decompress(data)
    if buf:
        print(buf)
    if decompressor.eof:
        print("End of stream")
        break
    data = input()

# Flush any remaining data
print(decompressor.flush())

# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Feed data to the compressor
data = b'This is the original text.'
compressed = compressor.compress(data)
print(compressed)

# Flush any remaining data
compressed += compressor.flush()
print(compressed)

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress the data
decompressed = decomp
