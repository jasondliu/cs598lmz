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
