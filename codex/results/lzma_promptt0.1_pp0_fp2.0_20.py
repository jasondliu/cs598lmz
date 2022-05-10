import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
data = b'.'
while True:
    # Feed data to the decompressor
    buf = decompressor.decompress(data)
    if buf:
        print(buf)
    if decompressor.eof:
        break
    data = b'.'

# Flush the decompressor
buf = decompressor.flush()
print(buf)

# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Compress some data
data = b'The quick brown fox jumps over the lazy dog.'
buf = compressor.compress(data)
print(buf)

# Flush the compressor
buf = compressor.flush()
print(buf)

# Test LZMAFile

# Compress a file
with open('lorem.txt', 'rb') as input, \
        lzma.open('lorem.txt.xz', 'wb')
