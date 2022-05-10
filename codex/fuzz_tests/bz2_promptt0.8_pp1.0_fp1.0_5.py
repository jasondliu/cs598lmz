import bz2
# Test BZ2Decompressor
# print(bz2.decompress(bz2_compressed))

# Test BZ2Compressor
# bz2_compressor = bz2.BZ2Compressor()
# result = bz2_compressor.compress(raw)
# result += bz2_compressor.flush()
# print(result)

# Experimenting with context manager
with open('lorem.txt', 'rt') as input, bz2.open('lorem.bz2', 'wt') as output:
    print('Done.')
