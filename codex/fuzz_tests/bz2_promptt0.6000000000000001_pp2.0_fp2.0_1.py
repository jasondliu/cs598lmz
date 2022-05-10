import bz2
# Test BZ2Decompressor.
decomp = bz2.BZ2Decompressor()
with open('../data/test.bz2', 'rb') as f:
    compressed = f.read(1024)
    uncompressed = decomp.decompress(compressed)
    print(uncompressed)

with open('../data/test.bz2', 'rb') as f:
    decomp = bz2.BZ2Decompressor()
    for block in iter(lambda : f.read(1024), b''):
        print(decomp.decompress(block))

# Test BZ2Compressor.
comp = bz2.BZ2Compressor()
uncompressed = b'This is an uncompressed string.'
compressed = comp.compress(uncompressed)
compressed += comp.flush()
print(compressed)

with open('../data/test.bz2', 'rb') as f:
    data = f.read()
    print(decomp.decompress(data))

comp = bz2.BZ2Compressor()
with open('
