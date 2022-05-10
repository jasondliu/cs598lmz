import bz2
# Test BZ2Decompressor

text = bz2.compress(b"Hello, world!")

decompressor = bz2.BZ2Decompressor()
d_data = decompressor.decompress(text)
print(d_data)
