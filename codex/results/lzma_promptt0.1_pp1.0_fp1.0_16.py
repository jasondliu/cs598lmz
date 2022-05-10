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
        decompressor.decompress(data)
        data = decompressor.unconsumed_tail
    if not data:
        print('No more data; waiting for more')
        data = yield
        if not data:
            raise StopIteration

# Get the result
result = decompressor.flush()
print('Decompressed data: %r' % result)

# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
data = decompressor.unconsumed_tail

# Feed data to the decompressor object
while True:
    if data:
        print('Feeding
