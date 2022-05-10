import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressed_data = decompressor.decompress(compressed_data)
print(decompressed_data)

# Test BZ2File
file_in = bz2.BZ2File('bz2_compressed.bz2', 'rb')
print(file_in.read())

# Test BZ2File with decompressor
file_in = bz2.BZ2File('bz2_compressed.bz2', 'rb')
decompressor = bz2.BZ2Decompressor()
uncompressed_data = decompressor.decompress(file_in.read())
print(uncompressed_data)

# Test BZ2File with context manager
with bz2.BZ2File('bz2_compressed.bz2', 'rb') as file:
    print(file.read())

# Test BZ2File with context manager and decompressor
with bz2.BZ2File('bz2_compressed.bz2',
