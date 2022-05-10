import bz2
# Test BZ2Decompressor
data = b'my bz2data.'

# Compress data
compressor = bz2.BZ2Compressor()
compressed = compressor.compress(data)
print(compressed)

# flush the compressor
flush = compressor.flush()
print(flush)

# Reset the compressor
compressor.reset()

# Decompress data
decompressor = bz2.BZ2Decompressor()
decompressed = decompressor.decompress(compressed + flush)
print(decompressed)
