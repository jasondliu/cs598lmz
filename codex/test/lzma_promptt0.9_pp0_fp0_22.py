import lzma
# Test LZMADecompressor with an input less than 23 bytes.  A LZMADecompressor
# with an input less than 23 bytes must return nothing.
from lzma import LZMADecompressor
d = LZMADecompressor()
