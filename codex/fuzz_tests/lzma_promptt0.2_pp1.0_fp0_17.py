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
        print('After decompression, %d bytes left in unconsumed_tail' % len(decompressor.unconsumed_tail))
        print('Decompressed data: %r' % data)
    if not data:
        print('No more data, flushing')
        data = decompressor.flush()
        print('After flush, %d bytes left in unconsumed_tail' % len(decompressor.unconsumed_tail))
        print('Flushed data: %r' % data)
    if not data:
        break

# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()


