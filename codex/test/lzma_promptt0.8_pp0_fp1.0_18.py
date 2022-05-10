import lzma
# Test LZMADecompressor
data = b"\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3]\xe7\x92\xe5\x92\xe1\x01\x00\x04\x04\tdatatest"
lzc = lzma.LZMADecompressor()
# This line raises a TypeError: can't use a string pattern on a bytes-like object
