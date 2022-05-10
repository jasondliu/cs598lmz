import lzma
# Test LZMADecompressor
lz = lzma.LZMADecompressor()
assert lz.decompress(b"x\x9cKLJ\x04\x00\x00\xff\xff") == b'hello'
assert lz.decompress(b"x\x9c\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff") == b'world'

# Test LZMADecompressor with bufsize
lz = lzma.LZMADecompressor(format=lzma.FORMAT_AUTO)
assert lz.decompress(b"x\x9cKLJ\x04\x00\x00\xff\xff", 8) == b'hello'
assert lz.decompress(b"x\x9c\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff") == b'world'

lz = lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
