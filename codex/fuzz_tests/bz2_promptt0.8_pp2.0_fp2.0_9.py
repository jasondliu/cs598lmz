import bz2
# Test BZ2Decompressor
# Read the file
fin = bz2.BZ2File("../data/amazon_reviews_us_Wireless_v1_00.tsv.bz2")
decompressor = bz2.BZ2Decompressor()
# ...
data = fin.read(10 * decompressor.decompress_size)
# ...
# Get the decompressed size
# ...
print(decompressor.decompress_size)

# Decompress data
# ...
decompress_size = decompressor.decompress_size
decompressed_data = decompressor.decompress(data)
# ...
# Repeat until finished (EOF)
# ...

# Test BZ2Compressor
# Initialize compressor
compressor = bz2.BZ2Compressor()
# Compress some data
compressed_data = compressor.compress(data)
# Flush the compressor
compressed_data += compressor.flush()
# Compress another file
# ...
# Flush the compressor
# ...
compressed_data += compressor.flush()
# ...
