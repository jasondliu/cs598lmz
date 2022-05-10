import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Test BZ2File
with bz2.BZ2File('example.bz2', 'wb') as output:
    for line in f:
        output.write(line)

with bz2.BZ2File('example.bz2', 'rb') as input:
    print(input.readline())

# Compress data incrementally
compressor = bz2.BZ2Compressor()
for line in f:
    data = compressor.compress(line)
    if data:
        print(data)
    else:
        print("Buffered")

remainder = compressor.flush()
print(remainder)
