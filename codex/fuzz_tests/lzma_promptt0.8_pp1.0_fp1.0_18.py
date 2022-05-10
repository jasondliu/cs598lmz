import lzma
# Test LZMADecompressor
lz = lzma.LZMADecompressor()
ret = lz.decompress(b'\x00')
assert(ret == b'')

ret = lz.decompress(b'\x00' * 3 + b'\x02' * 3)
assert(ret == b'\x00' * 3 + b'\xff' * 3)

ret = lz.decompress(b'\x00' * 2 + b'\x01' * 2 + b'\x02' * 2)
assert(ret == b'\x00' * 2 + b'\xff' * 2 + b'\xfe' * 2)

ret = lz.decompress(b'\x00' * 6)
assert(ret == b'\x00' * 6)

print('Tests successful')
