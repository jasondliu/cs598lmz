import lzma
# Test LZMADecompressor output when we read the entire source at once.

t = b'this is a test'

e = lzma.compress(t)
s = lzma.LZMADecompressor().decompress(e)

print(s)
compress = lzma.compress
