import bz2
# Test BZ2Decompressor.decompress() with the limit parameter.

# Decompress a small file in chunks.
with bz2.open("bz2_file", "rb") as infile:
    d = bz2.BZ2Decompressor()
    data = d.decompress(infile.read(100), limit=3)
    data += d.decompress(infile.read(), limit=3)
    print(data)
# Decompress a large file in chunks.
with bz2.open("bz2_file", "rb") as infile:
    d = bz2.BZ2Decompressor()
    data = d.decompress(infile.read(100), limit=0)
    data += d.decompress(infile.read(), limit=0)
    print(data)
# Create a compressor and decompress the data in one go.
with bz2.open("bz2_file", "rb") as infile:
    d = bz2.BZ2Decompressor()
    data = d.decompress
