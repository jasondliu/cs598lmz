import lzma
# Test LZMADecompressor object.
c = lzma.LZMACompressor()
compressed = c.compress(b'1234567890abcdefgh')
print(compressed)

c.flush()
print(c.compress(b'ij'))
print(c.compress(b'kl'))
print(c.compress(b'mn'))
print(c.compress(b'op'))
print(c.compress(b'qr'))
print(c.compress())
print(c.compress())

d = lzma.LZMADecompressor()
print(d.decompress(compressed))
print(d)
print(d.decompress(c.compress(b'stuvwxyz')))


# Test incremental decompression.
c = lzma.LZMACompressor()
compressed1 = c.compress(b'1234567890abcdef')
compressed2 = c.compress(b'1234567890')
compressed3 = c.compress(b'12345')
