import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

with open('data/example4.bz2', 'rb') as input:
    with open('data/uncompressed.txt', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))

# Test BZ2File
with bz2.BZ2File('data/example4.bz2') as input:
    with open('data/uncompressed.txt', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(block)

# Compress data
data = b'Lots of data here.'
compressor = bz2.BZ2Compressor()
result = bytearray()
for block in [data[i:i + 1024] for i in range(0, len(data), 1024)]:
    result.extend(compressor.compress(block))
result.extend(comp
