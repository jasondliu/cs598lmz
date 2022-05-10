import bz2
# Test BZ2Decompressor
c = bz2.BZ2Compressor()
print("Compressor: ", c)
d = bz2.BZ2Decompressor()
print("Decompressor: ", d)

print("\nCompressing and decompressing data ...")
data = b"This is a lot of data!" * 1000
print("Original data:")
print(" ".join("{:02x}".format(i) for i in data))
compressed = c.compress(data)
print("\nCompressed data:")
print(" ".join("{:02x}".format(i) for i in compressed))
decompressed = d.decompress(compressed)
print("\nDecompressed data:")
print(" ".join("{:02x}".format(i) for i in decompressed))
print("\nDecompressed equals original:", decompressed == data)

print("\nDecompressing the compressed data all at once ...")
