import lzma
# Test LZMADecompressor
#
# This test is intended to be run with a single command line argument, which
# should be the name of a file containing a single compressed stream.
#
# The test will read the file and decompress it using the LZMADecompressor
# class.  The decompressed data will be compared against the original data.
#
# The test will also decompress the input data in chunks of various sizes
# and compare the results.

# Read the entire input file
