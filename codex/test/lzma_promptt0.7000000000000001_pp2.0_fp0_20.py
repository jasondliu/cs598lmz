import lzma
# Test LZMADecompressor.
# Test that we can decompress a valid lzma stream.  We use the lzma_alone
# example from the XZ SDK and decompress it with our pure-Python
# LZMADecompressor.

# This example has been encoded to be able to be embedded in a C program.
# The first 18 bytes are the header.  The rest is the compressed data.

# The decompressed data is the following string:
# "This is the example text for LZMA Utils. "
# "It is just a simple text file. "
# "You can also compress it with LZMA Utils. "
# "It is not very long, but it does not have to be. "
# "You can use any size of file you want. "
# "The LZMA compressor (xz) can compress files of any size."

# This example has been compressed with LZMA Utils 4.32.7 and
# lzma_alone with default options.

