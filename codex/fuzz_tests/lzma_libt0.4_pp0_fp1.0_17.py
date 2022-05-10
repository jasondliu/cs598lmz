import lzma
lzma.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')

# lzma.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/lib/python3.6/lzma.py", line 593, in decompress
#     return LZMADecompressor().decompress(data)
#   File "/usr/lib/python3.6/lzma.py", line 583, in decompress
#     return self.decompressobj
