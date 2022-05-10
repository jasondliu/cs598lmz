import bz2
# Test BZ2Decompressor

dec = bz2.BZ2Decompressor()

with open('output/enwik8.bz2', 'rb') as f:
    first_chunk = f.read(2048)
    print(dec.decompress(first_chunk))

# Test BZ2File

with bz2.BZ2File('output/enwik8.bz2', 'r') as f:
    print(f.readlines()[:5])

# Test BZ2Compressor

comp = bz2.BZ2Compressor()

with open('output/enwik8.bz2', 'rb') as f:
    first_chunk = f.read(2048)
    compressed = comp.compress(first_chunk)
    print(compressed)

# Test BZ2File

with bz2.BZ2File('output/enwik8.bz2', 'w') as f:
    f.write(compressed)

# Test BZ2File.readline

with bz2.
