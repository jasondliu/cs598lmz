from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x00' * 5)

# Issue #12076: LZMADecompressor.decompress() should raise an error
# when given an empty byte string.
