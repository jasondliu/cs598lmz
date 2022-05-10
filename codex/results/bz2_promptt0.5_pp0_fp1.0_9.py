import bz2
# Test BZ2Decompressor

data = open('test.bz2', 'rb').read()
decompressor = bz2.BZ2Decompressor()

for i in range(0, len(data), 100):
    block = data[i:i+100]
    if block:
        print(decompressor.decompress(block))
    else:
        print(decompressor.flush())

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
for i in range(0, len(data), 100):
    block = data[i:i+100]
    if block:
        print(compressor.compress(block))
    else:
        print(compressor.flush())
