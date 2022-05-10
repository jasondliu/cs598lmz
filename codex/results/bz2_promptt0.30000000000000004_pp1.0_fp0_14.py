import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Test BZ2File
with bz2.BZ2File('data.bz2') as f:
    print(f.read())

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()

# Test BZ2File
with bz2.BZ2File('data.bz2', 'w') as f:
    f.write(data)
