import lzma
lzma.decompress(lzma.compress(b'abc'))

# decompress
lzma.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6B\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x00\x04')

# compress
lzma.compress(b'abc')
