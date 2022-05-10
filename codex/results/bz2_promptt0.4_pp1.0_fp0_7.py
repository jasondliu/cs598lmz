import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()

with open('data/data.bz2', 'rb') as f:
    data = f.read()

decompressed = bz2_decompressor.decompress(data)

print(decompressed)

# Test BZ2File

with bz2.BZ2File('data/data.bz2') as f:
    print(f.read())
