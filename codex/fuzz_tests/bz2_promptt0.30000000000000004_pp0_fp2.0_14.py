import bz2
# Test BZ2Decompressor

bz_comp = bz2.BZ2Compressor()
bz_decomp = bz2.BZ2Decompressor()

data = b'hello world'

compressed = bz_comp.compress(data)
print(compressed)

decompressed = bz_decomp.decompress(compressed)
print(decompressed)

# Test BZ2File

with bz2.BZ2File('test.bz2', 'w') as f:
    f.write(data)

with bz2.BZ2File('test.bz2', 'r') as f:
    print(f.read())
