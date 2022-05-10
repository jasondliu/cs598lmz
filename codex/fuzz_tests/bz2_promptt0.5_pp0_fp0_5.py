import bz2
# Test BZ2Decompressor
bz2_decompressor = bz2.BZ2Decompressor()
decompressed_data = bz2_decompressor.decompress(compressed_data)
print(decompressed_data)

# Test BZ2File
with bz2.BZ2File('bz2_text.bz2', 'wb') as file:
    file.write(text)
with bz2.BZ2File('bz2_text.bz2', 'rb') as file:
    print(file.read())

# Test compress and decompress
compressed_data = bz2.compress(text)
print(bz2.decompress(compressed_data))
