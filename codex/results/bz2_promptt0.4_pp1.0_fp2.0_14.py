import bz2
# Test BZ2Decompressor

compressor = bz2.BZ2Compressor()
decompressor = bz2.BZ2Decompressor()

data = b"Lots of content here"

compressed = compressor.compress(data)

print("Compressed: {}".format(len(compressed)))
print("Decompressed: {}".format(len(decompressor.decompress(compressed))))

compressed += compressor.flush()
print("Final compressed length: {}".format(len(compressed)))
print("Decompressed: {}".format(len(decompressor.decompress(compressed))))

# decompressor = bz2.BZ2Decompressor()
# decompressor.decompress(compressed)
# decompressor.unused_data

# decompressor = bz2.BZ2Decompressor()
# decompressor.decompress(compressed)
# decompressor.unused_data

# decompressor = bz2.BZ2Decompressor()
# decompressor.decompress(compressed)
# decompressor.unused_
