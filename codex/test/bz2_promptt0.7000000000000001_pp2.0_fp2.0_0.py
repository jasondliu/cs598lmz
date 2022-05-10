import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
compr = bz2.compress(b'hello')
compr += b'a' * (1024 - len(compr))
print(decompressor.decompress(compr))
