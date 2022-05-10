import lzma
# Test LZMADecompressor class against a known good test file.
# Test file came from LZMA SDK 4.42, LzmaUtil/LzmaUtil.c,
# function TestLzma().

# NOTE: the test file is binary.  Conversely, you could run
# the test file through test_lzma.py to produce a .xz file
# to read and write.

# This test file corresponds to the original arg_struct settings
# of {5, {0, 0}, {0, 0}, 0, 0x20, 0, 0, 1, 0, 0, 0};
# NOTE: the block size is small, so you can't read partial blocks!

# This test file is from Python 3.2.2, Lib/test/test_lzma.py

CompLzma = '99999999963'
CompLzma = CompLzma.encode('ascii')

LZMA_HEADER_SIZE = 14
