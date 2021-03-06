import lzma
lzma.decompress(b"\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

# decompress doesn't check the magic number
# so it works on xz-compressed files as well
lzma.decompress(b"\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

# decompress doesn't check the magic number
# so it works on raw lzma files as well
lzma.decompress(b
