import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Test BZ2File
with bz2.BZ2File('compressed_file.bz2', 'wb') as f:
    f.write(compressed_data)
with bz2.BZ2File('compressed_file.bz2', 'rb') as f:
    data = f.read()
    print(data)

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()

# Test bz2.compress()
bz2.compress(data)

# Test bz2.decompress()
bz2.decompress(compressed_data)
