import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
data = decompressor.unconsumed_tail

# Feed data to the decompressor object
while True:
    if data:
        print('Feeding %d bytes to the decompressor' % len(data))
        data = decompressor.decompress(data)
        print('After feed, %d bytes left in unconsumed_tail' % len(decompressor.unconsumed_tail))
        print('Decompressed data: %r' % data)
    if not data:
        break

# Flush the decompressor object
data = decompressor.flush()
print('flushed: %r' % data)

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
data = decompressor.unconsumed_tail

# Feed data to the decompressor object
while True:
    if data:
        print('Feeding %
