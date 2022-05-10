import lzma
# Test LZMADecompressor
data = b'this is the original data'

cdata = lzma.compress(data)
print(len(data), len(cdata))

d = lzma.LZMADecompressor()
print(d.decompress(cdata))

print(d.decompress(b'\x00'))
print(d.flush())

print(d.decompress(b''))
print(d.flush())

print(d.decompress(b'\xff'))
print(d.flush())

print(d.decompress(b'\xff'))
print(d.flush())

print(d.decompress(b'\xff'))
print(d.flush())

print(d.decompress(b'\xff'))
print(d.flush())

print(d.decompress(b'\xff'))
print(d.flush())

print(d.decompress(b'\xff'))
print(d.flush())

print(d.decompress
