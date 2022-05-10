import bz2
# Test BZ2Decompressor
decomp = bz2.BZ2Decompressor()

with open('data/enwik9.bz2', 'rb') as f:
    print(decomp.decompress(f.read(1024)))

with open('data/enwik9.bz2', 'rb') as f:
    print(decomp.decompress(f.read(1024)))

with open('data/enwik9.bz2', 'rb') as f:
    print(decomp.decompress(f.read(1024)))

with open('data/enwik9.bz2', 'rb') as f:
    print(decomp.decompress(f.read(1024)))

with open('data/enwik9.bz2', 'rb') as f:
    print(decomp.decompress(f.read(1024)))

with open('data/enwik9.bz2', 'rb') as f:
    print(decomp.decompress(f.read(1024)))

with open('data/enwik9.bz
