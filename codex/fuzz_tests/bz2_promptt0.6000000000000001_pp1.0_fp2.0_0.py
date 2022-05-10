import bz2
# Test BZ2Decompressor
with bz2.BZ2File('data/file.bz2', 'r') as f:
    file_content = f.read()
    print(file_content.decode('utf-8'))

decompressor = bz2.BZ2Decompressor()
with open('data/file.bz2', 'rb') as f:
    file_content = f.read()
    print(decompressor.decompress(file_content).decode('utf-8'))

with bz2.open('data/file.bz2', 'r') as f:
    file_content = f.read()
    print(file_content.decode('utf-8'))

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
with open('data/file', 'rb') as f:
    file_content = f.read()
    compressed_content = compressor.compress(file_content)
    print(compressed_content)

with bz2.open('data/file.bz2
