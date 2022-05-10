import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data.bz2', 'rb') as input:
    with open('data.out', 'wb') as output:
        for block in iter(lambda: input.read(1024 * 1024), b''):
            output.write(decompressor.decompress(block))

# Compress data

data = b'Lots of data here'

compressor = bz2.BZ2Compressor()

with open('data.bz2', 'wb') as output:
    for i in range(100):
        output.write(compressor.compress(data))
    output.write(compressor.flush())
 
# Compress data in memory

data = b'Lots of data here'

compressed = bz2.compress(data)

print(len(data))
print(len(compressed))

decompressed = bz2.decompress(compressed)

print(data == decompressed)

# Compress data using context manager

data
