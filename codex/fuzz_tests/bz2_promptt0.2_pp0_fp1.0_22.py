import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content)
    print(decompressor.decompress(file_content))

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/sample.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content)
    print(compressor.compress(file_content))

# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content)

with bz2.BZ2File('data/sample.bz2', 'wb') as f:
    f.write(b'Hello World!')

with bz2.BZ2File('data/sample.bz2', '
