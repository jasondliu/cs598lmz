from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

# bz2.decompress() also accepts a max_length parameter
# to limit the amount of data returned
bz2.decompress(compressed_data, max_length=100)
 
# Note that decompress() does not know the original
# length of the uncompressed data, and will return as much
# data as possible.  If you know the original length of the
# uncompressed data, you can pass it to decompress() to
# prevent it from returning more than that amount of data.
bz2.decompress(compressed_data, max_length=100)

# The BZ2Decompressor class also provides a read() method
# that can be used to read data chunk-by-chunk.
# This is useful when the compressed data is stored in
# a file-like object
decompressor = BZ2Decompressor()
decompressor.decompress(compressed_data[:100])
decompressor.decompress(compressed_data[100:])
decompressor.decompress(comp
