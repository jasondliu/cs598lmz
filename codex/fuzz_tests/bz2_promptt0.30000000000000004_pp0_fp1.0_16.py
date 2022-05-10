import bz2
# Test BZ2Decompressor
data = open('lorem.txt', 'rb').read()

compressor = bz2.BZ2Compressor()
print(compressor.compress(data))
print(compressor.flush())

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(compressor.compress(data) + compressor.flush()))

# Test BZ2File
bz_file = bz2.BZ2File('lorem.txt.bz2', 'wb')
bz_file.write(data)
bz_file.close()

bz_file = bz2.BZ2File('lorem.txt.bz2', 'rb')
print(bz_file.read())
bz_file.close()

# Test compress() and decompress()
compressed = bz2.compress(data)
print(compressed)
print(bz2.decompress(compressed))

# Test open()
bz_file = bz2.open('lorem.txt.
