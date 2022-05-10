import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
data = b"x"
while True:
    # Feed one byte at a time into decompressor
    buf = decompressor.decompress(data)
    if buf:
        print(buf)
    if decompressor.eof:
        break
    data = sys.stdin.buffer.read(1)

# Flush the decompressor
buf = decompressor.flush()
print(buf)

# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Read one byte, just to kick things off
data = b"x"
while True:
    # Feed one byte at a time into compressor
    buf = compressor.compress(data)
    if buf:
        print(buf)
    data = sys.stdin.buffer.read(1)
    if not data:
        break

# Flush the compressor
buf = compressor.flush()
