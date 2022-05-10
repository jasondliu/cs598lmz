import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
data = b'.'
while True:
    # Feed one byte at a time into decompressor
    buf = decompressor.decompress(data)
    if buf:
        print(buf)
    if decompressor.eof:
        break
    data = b'.'

# Flush the decompressor
buf = decompressor.flush()
if buf:
    print(buf)

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
data = b'.'
while True:
    # Feed one byte at a time into decompressor
    buf = decompressor.decompress(data)
    if buf:
        print(buf)
    if decompressor.eof:
        break
    data = b'.'

# Flush the decompressor
buf = decompressor.flush()
if buf:
    print(buf)
