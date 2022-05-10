import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()
data = decompressor.decompress(bz2_data)
data == original_data

# Test BZ2File

with bz2.BZ2File('lorem.txt.bz2', 'wb') as output:
    with open('lorem.txt', 'rb') as input:
        output.write(input.read())

with bz2.BZ2File('lorem.txt.bz2', 'rb') as input:
    print(input.readline())

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
output = compressor.compress(original_data)
output += compressor.flush()
len(output)

# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()
decompressor.decompress(output)

# Test BZ2File

with bz2.BZ2File('lorem.txt.bz2', 'rb') as input
