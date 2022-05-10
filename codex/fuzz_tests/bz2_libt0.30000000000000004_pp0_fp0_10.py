import bz2
bz2.BZ2File(filename)

# To read the entire file as a single byte string, use bz2.decompress()
uncompressed_data = bz2.decompress(bz2_data)

# To compress a chunk of data, you can use bz2.compress()
bz2_data = bz2.compress(raw_data)

# The bz2 module includes a convenience function, open(), that works like the open()
# function in the built-in open(), but handles the compression and decompression
# automatically
bz2_file = bz2.open(filename, mode)

# The bz2 module also includes a BZ2Compressor and BZ2Decompressor class, which
# can be used for incremental compression and decompression
compressor = bz2.BZ2Compressor()
decompressor = bz2.BZ2Decompressor()

# The compress() and decompress() methods of both classes return chunks of data
# as bytes objects.
compressed_data = compressor.compress(data)
decomp
