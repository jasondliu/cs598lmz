import bz2
# Test BZ2Decompressor

# Test that a decompressor can decompress data in chunks of arbitrary size
# (i.e. test the incremental decompression functionality)

data = bz2.compress(b"this is a test")

decomp = bz2.BZ2Decompressor()

# decompress the data in chunks of varying size
for chunk_size in range(1, len(data)):
    result = decomp.decompress(data[:chunk_size])
    data = data[chunk_size:]
    if not result:
        break

# decompress any remaining data
result += decomp.decompress(data)
