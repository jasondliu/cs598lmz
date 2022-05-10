import lzma
# Test LZMADecompressor.

d = lzma.LZMADecompressor()
compr = lzma.compress('The quick brown fox jumps over the lazy dog.'.encode('ascii'))
uncompr = d.decompress(compr)
uncompr

offset = 10
chunk = 16
context = b'and the usual '

compr2 = compr[offset:]
# ... filter ...
uncompr2 = d.decompress(compr2, max_length=chunk)
print(context + uncompr2)
d.unused_data

print(d.flush())
print(d.unused_data)

print(d.flush())
d.unused_data

print(uncompr)
# Test LZMADecompressor object as a context manager.

with lzma.LZMADecompressor() as d:
    x = b''.join([d.decompress(compr),
                  d.flush()])

print(x)
print(d.unused_data)
x =
