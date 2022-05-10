import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(compressed_data))

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
print(compressor.compress(data))
print(compressor.flush())

# Test bz2.open()
print(bz2.open('lorem.txt.bz2').read())

# Test bz2.compress() and bz2.decompress()
print(bz2.compress(data))
print(bz2.decompress(compressed_data))

# Test bz2.BZ2File
with bz2.BZ2File('lorem.txt.bz2') as input:
    print(input.read())

with bz2.BZ2File('lorem.txt.bz2', 'w') as output:
    output.write(data)

# Test bz2.BZ2Compressor and bz2.BZ2Decompressor
comp
