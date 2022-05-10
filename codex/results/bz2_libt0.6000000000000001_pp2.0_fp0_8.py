import bz2
bz2_comp = bz2.BZ2Compressor()
data = b"this is the original uncompressed data".encode("utf-8")
len(data)

# compress the data
compressed_data = bz2_comp.compress(data)
len(compressed_data)

# flush the compressor which finishes its internal buffering
more_compressed_data = bz2_comp.flush()
len(more_compressed_data)

# the compressed data is much smaller than the original

# create a decompressor object
bz2_decomp = bz2.BZ2Decompressor()

# decompress the data
decompressed_data = bz2_decomp.decompress(compressed_data + more_compressed_data)
len(decompressed_data)

# the decompressed data is the same as the original
decompressed_data == data

# create a compressor object and compress the data in one step
compressed_data = bz2.compress(data)
len(compressed_data)

# the compressed
