import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Test BZ2File
with bz2.BZ2File(compressed_file, 'wb') as f:
    f.write(original_data)

with bz2.BZ2File(compressed_file, 'rb') as f:
    print(f.read())

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
compressor.compress(original_data)
compressor.flush()

# Test BZ2File
with bz2.BZ2File(compressed_file, 'wb') as f:
    f.write(original_data)

with bz2.BZ2File(compressed_file, 'rb') as f:
    print(f.read())
