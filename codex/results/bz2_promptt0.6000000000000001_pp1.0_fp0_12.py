import bz2
# Test BZ2Decompressor
decomp = bz2.BZ2Decompressor()
print(decomp.decompress(comp))

# Test BZ2File
with bz2.BZ2File('data.bz2', 'rb') as f:
    print(f.readline())

# Test BZ2Compressor
comp = bz2.BZ2Compressor()
print(comp.compress(data))
print(comp.flush())
