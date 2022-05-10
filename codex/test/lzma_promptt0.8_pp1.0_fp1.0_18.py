import lzma
# Test LZMADecompressor
lz = lzma.LZMADecompressor()
ret = lz.decompress(b'\x00')
assert(ret == b'')

ret = lz.decompress(b'\x00' * 3 + b'\x02' * 3)
