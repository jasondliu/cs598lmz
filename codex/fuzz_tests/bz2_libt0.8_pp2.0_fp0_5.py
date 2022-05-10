import bz2
bz2.decompress(bz2.BZ2Compressor().compress(INPUT_DATA)) == INPUT_DATA

# Use the BZ2Decompressor object directly.
compressor = bz2.BZ2Compressor()
decompressor = bz2.BZ2Decompressor()

compressed = compressor.compress(INPUT_DATA)
compressed += compressor.flush()

print decompressor.decompress(compressed)
print

# Writing in chunks.
compressor = bz2.BZ2Compressor()
data = []

for i in range(5):
    data.append(compressor.compress(INPUT_DATA))
    
data.append(compressor.flush()) # Must flush before calling the decompressor.

decompressor = bz2.BZ2Decompressor()

for chunk in data:
    # Check the chunks of compressed data as we decompress them.
    print decompressor.decompress(chunk)

print '%d bytes of compressed data generated.' % len(compressed)
print '
