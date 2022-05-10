import lzma
# Test LZMADecompressor
#
# This test was written to check that the LZMA decompressor is
# able to decompress files compressed with the XZ Utils.
#
# The test file was created with the XZ Utils 5.0.0 beta
# with the command:
#
#     xz -k -9e testdata/lorem
#
# The test file was then modified to add a header that is not
# recognized by the XZ Utils.
#
# The test file was created by Lasse Collin.

# The uncompressed test data
