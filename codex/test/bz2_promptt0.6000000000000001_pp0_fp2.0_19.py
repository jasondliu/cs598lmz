import bz2
# Test BZ2Decompressor with multiple input streams
# Not using a file, as that would require a file that is compressed with bz2,
# and the file compression is different than the stream compression.
d = bz2.BZ2Decompressor()
