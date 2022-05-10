import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(bz2_data))

print(decompressor.decompress(bz2_data))

print(decompressor.decompress(bz2_data))

print(decompressor.decompress(bz2_data))

print(decompressor.decompress(bz2_data))

print(decompressor.decompress(bz2_data))

print(decompressor.flush())


import bz2
# Test BZ2File
with bz2.BZ2File('lorem.txt.bz2', 'rb') as input:
    print(input.read())

with bz2.BZ2File('lorem.txt.bz2', 'rb') as input:
    print(input.readlines())

with bz2.BZ2File('lorem.txt.bz2', 'wb') as output:
    output.write(bz2_data)

