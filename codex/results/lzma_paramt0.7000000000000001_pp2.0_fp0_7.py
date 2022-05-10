from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# decompress the data
decompressed = blosc.decompress(data)
print(decompressed)

# decompress the data
decompressed = snappy.decompress(data)
print(decompressed)

# decompress the data
decompressed = zlib.decompress(data)
print(decompressed)

# decompress the data
decompressed = bz2.decompress(data)
print(decompressed)

# decompress the data
decompressed = lzma.decompress(data)
print(decompressed)

# decompress the data
decompressed = lz4.decompress(data)
print(decompressed)

# decompress the data
decompressed = zstd.decompress(data)
print(decompressed)
