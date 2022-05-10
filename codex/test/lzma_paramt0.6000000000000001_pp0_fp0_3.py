from lzma import LZMADecompressor
LZMADecompressor.decompress

# Test the LZMADecompressor.flush() method doesn't crash on errors.
# See https://bugs.python.org/issue23405
