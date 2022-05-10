import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()
d = decompressor.decompress(compressed_data)
print(d.decode('utf-8'))

# To prove that the BZ2 compressed data is a good representation of the original uncompressed data,
# let’s check whether decompressed data and the original data are the same:

print(d == data)

# This is a very small example of how to work with BZ2 compressed data.
# However, usually, if you want to compress a large file, you want to work with files that are much larger than the amount of available RAM.
# In such a case, you should use the BZ2File class.


# bz2.BZ2File

# The BZ2File class is a thin wrapper around the BZ2Compressor and BZ2Decompressor classes.
# It compresses data chunks read from a file object and writes the compressed data to another file object.
# Likewise, it decompresses data chunks read from a file object and writes the decompressed data to another file object.

# Here
