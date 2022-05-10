import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

with open('compressed.bz2', 'rb') as f:
    file_content = f.read()

uncompressed_data = decompressor.decompress(file_content)
uncompressed_data

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()

with open('compressed.bz2', 'rb') as f:
    file_content = f.read()

compressed_data = compressor.compress(file_content)
compressed_data

# Test BZ2File
with bz2.BZ2File('compressed.bz2') as f:
    file_content = f.read()

file_content

# Test BZ2File
with bz2.BZ2File('compressed.bz2', 'w') as f:
    f.write(file_content)

# Test BZ2File
with bz2.BZ2File('compressed.bz2', 'r')
