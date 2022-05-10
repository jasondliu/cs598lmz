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
testdata = b"""Lorem ipsum dolor sit amet, consectetuer adipiscing
elit. Maecenas porttitor congue massa. Fusce posuere, magna sed
pulvinar ultricies, purus lectus malesuada libero, sit amet
commodo magna eros quis urna.
Nunc viverra imperdiet enim. Fusce est. Vivamus a tellus.
Pellentesque habitant morbi tristique senectus et netus
et
