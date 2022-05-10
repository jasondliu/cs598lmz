from lzma import LZMADecompressor
LZMADecompressor.decompress

# Test the LZMADecompressor.flush() method doesn't crash on errors.
# See https://bugs.python.org/issue23405
with LZMADecompressor() as c:
    c.flush(0)

# Test that LZMADecompressor.decompress() raises a ValueError if the
# input string is larger than 2 GiB.
# See https://bugs.python.org/issue23405
with LZMADecompressor() as c:
    with self.assertRaises(ValueError):
        c.decompress(b'\x00' * (2**31 + 1))

# Test that LZMADecompressor.flush() raises a ValueError if the
# output buffer size is larger than 2 GiB.
# See https://bugs.python.org/issue23405
with LZMADecompressor() as c:
    with self.assertRaises(ValueError):
        c.flush(2**31 + 1)

# Test that LZMADecompressor.decompress
