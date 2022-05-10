import bz2
# Test BZ2Decompressor
data = open('../data/sample.bz2', 'rb').read()

decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
result

# Test BZ2File
bz_file = bz2.BZ2File('../data/sample.bz2')
result = bz_file.read()
result

bz_file = bz2.BZ2File('../data/sample.bz2')
for line in bz_file:
    print(line)

# Compress data
data = open('../data/lorem.txt', 'rb').read()

compressor = bz2.BZ2Compressor()
result = compressor.compress(data)
result += compressor.flush()

open('../data/lorem.bz2', 'wb').write(result)
