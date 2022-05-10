from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# Compress data
data = b'This is the original text.'
len(data)

bz2_data = bz2.compress(data)
len(bz2_data)

bz2.decompress(bz2_data)

# Compress data incrementally
data = b'This is the original text.'
len(data)

compressor = bz2.BZ2Compressor()
result = []

for block in [data[0:5], data[5:15], data[15:]]:
    result.append(compressor.compress(block))

result.append(compressor.flush())

bz2_data = b''.join(result)
len(bz2_data)

bz2.decompress(bz2_data)

# Decompress data incrementally
bz2_data = bz2.compress(data)
len(bz2_data)

decompressor = bz2.BZ2Decompressor()
