import lzma
lzma.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# The output is a byte string:
# b'The quick brown fox jumps over the lazy dog.'

# When we use the compress() function, we get a byte string as well:

lzma.compress(b'The quick brown fox jumps over the lazy dog.')

# b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00'
