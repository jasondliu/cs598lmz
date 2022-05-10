import bz2
# Test BZ2Decompressor.
#
# In order to test the BZ2Decompressor, we need to create a decompressor
# object, feed it some data, and then read from it to see if the correct
# data is returned.  We can't really use any of the existing test data,
# because it's not guaranteed to be valid BZ2 data.
#
# So, what we do is create a BZ2Compressor object, write some data to
# it, and then read back the compressed data and decompress it with the
# BZ2Decompressor object.  The data we write is carefully crafted to be
# valid BZ2 data, but not necessarily the kind of data that BZ2Compressor
# would produce.
#
# The data we write consists of the following:
# - The BZ2 header
# - A valid BZ2 block header
# - A zero-length block (which is valid)
# - A valid BZ2 block header
# - The data "Hello, world!"
# - A valid BZ2 block header
# - The data "Goodbye, world!"
# - The BZ2 E
