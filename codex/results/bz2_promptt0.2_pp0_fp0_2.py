import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Test BZ2File
with bz2.BZ2File('data.bz2', 'wb') as f:
    f.write(compressed_data)

with bz2.BZ2File('data.bz2', 'rb') as f:
    print(f.read())

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()

# Test compress()
compressed_data = bz2.compress(data)

# Test decompress()
decompressed_data = bz2.decompress(compressed_data)

# Test open()
with bz2.open('data.bz2', 'wb') as f:
    f.write(data)

with bz2.open('data.bz2', 'rb') as f:
    print(f.read())

#
