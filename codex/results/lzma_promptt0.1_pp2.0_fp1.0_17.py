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
    data = input()

# Flush the decompressor
buf = decompressor.flush()
print(buf)

# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Read one byte, just to kick things off
data = b'.'
while True:
    # Feed data to the compressor
    buf = compressor.compress(data)
    if buf:
        print(buf)
    data = input()

# Flush the compressor
buf = compressor.flush()
print(buf)

# Test LZMAFile

# Open a file for reading
with lzma.open('file.xz', '
