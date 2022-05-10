import lzma
# Test LZMADecompressor
data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'
d = lzma.LZMADecompressor()
d.decompress(data)
d.decompress(b'')
d.decompress(b'\x00')
d.decompress(b'\x00')
d.decompress(b'\x00')
d.decompress(b'\x00')
d.decompress(b'\x00')
d.decompress(b'\x00')
d.decompress(b'\x00')
d.decompress(b'\x00')
d.decompress(b'\x00')
d.decompress(b'\x00')
d.decompress(b'\x00')
d.decompress(b'\x
