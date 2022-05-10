import lzma
# Test LZMADecompressor by feeding it bytes and compare the result to the
# reference implementation xz.
#
# The data is compressed with xz using the same options as used in
# test_lzmaffi.py.

# Generate a random test case.
