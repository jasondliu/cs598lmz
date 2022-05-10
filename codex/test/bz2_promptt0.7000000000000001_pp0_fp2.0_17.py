import bz2
# Test BZ2Decompressor.readinto(size)
import io
import sys
import bz2
import gc

# BZ2Decompressor.readinto(size) successfully reads 'size' bytes
# This test is an adaptation of test_bz2.BZ2FileTest.testRead10.
# Its purpose is to test the readinto(size) method of BZ2Decompressor.
# test_bz2.BZ2FileTest.testRead10 has a similar purpose for BZ2File.readinto(size)
# This test checks that BZ2Decompressor.readinto(size) returns the correct number
# of bytes in the 'size' parameter.
# If the file is a multiple of 'size', then 'size' bytes are returned for each call
# until the last one.
# If the file is not a multiple of 'size', then 'size' bytes are returned for each
# call except the last one.

# Test BZ2Decompressor.readinto(size)
# The file content is a multiple of 'size'

size = 256
