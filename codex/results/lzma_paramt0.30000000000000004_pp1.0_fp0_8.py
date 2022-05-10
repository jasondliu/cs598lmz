from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x00' * 5)

# Issue #12076: LZMADecompressor.decompress() should raise an error
# when given an empty byte string.
with pytest.raises(ValueError):
    LZMADecompressor().decompress(b'')

# Issue #12076: LZMADecompressor.decompress() should raise an error
# when given a byte string with an invalid header.
with pytest.raises(ValueError):
    LZMADecompressor().decompress(b'\x00' * 4)

# Issue #12076: LZMADecompressor.decompress() should raise an error
# when given a byte string with an invalid header.
with pytest.raises(ValueError):
    LZMADecompressor().decompress(b'\x00' * 6)

# Issue #12076: LZMADecompressor.decompress() should raise an error
# when given a byte string with an invalid header.

