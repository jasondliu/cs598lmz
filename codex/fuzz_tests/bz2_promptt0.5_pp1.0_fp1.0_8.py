import bz2
# Test BZ2Decompressor
#
# This is a test script for the decompressor object.
# It reads the test data (compressed and uncompressed) from
# the file 'decompressobj.testdata' and compares the result
# of decompressing the compressed data with the uncompressed
# data.
#
# The test data was created by running the program 'make_testdata.py'.
#
# The test data file has the following format:
#
# int: file size
# int: block size
# int: member size
# int: number of members
#
# for each member:
#   int: length of compressed data
#   int: length of uncompressed data
#   string: compressed data
#   string: uncompressed data
#
# The test data file was created using the following parameters:
#
# file size: 1000000
# block size: 900000
# member size: 1000000
# number of members: 1
#
# The test data consists of a single member that is a bzip2 compressed
# version of the file /usr/share/dict/words.
#
# The bzip2 compressed data was
