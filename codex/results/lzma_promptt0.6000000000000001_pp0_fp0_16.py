import lzma
# Test LZMADecompressor
d = lzma.LZMADecompressor()
print(d.decompress(b'XZ\xfd\xfd\x9c\x58\x00\x00\x04\xec\x00\xff\xff\x04\x00\x00\x00\x00\x00'))

# Test LZMACompressor
c = lzma.LZMACompressor()
print(c.compress(b'hello world'))
print(c.flush())

# Test open
with lzma.open('test.xz', 'w') as f:
    f.write(b'hello world')
