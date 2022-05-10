from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2.open()
with bz2.open('example.bz2', 'rt') as input:
    print(input.read())

# bz2.compress()
data = b'This is the original text.'
len(data)
compressed = bz2.compress(data)
len(compressed)

# bz2.decompress()
original = bz2.decompress(compressed)
original

# bz2.compresslevel()
for i in range(1, 10):
    print('{} : {}'.format(i, len(bz2.compress(data, i))))

# bz2.BZ2Compressor()
compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()

# bz2.BZ2Decompressor()
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed)
decompressor.
