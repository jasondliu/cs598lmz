import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as f:
    file_content = f.read()
    print(decompressor.decompress(file_content))

# Test BZ2File
with bz2.BZ2File('data/sample.bz2') as f:
    print(f.read())

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()

with open('data/sample.bz2', 'rb') as f:
    file_content = f.read()
    print(compressor.compress(file_content))
    print(compressor.flush())

# Test BZ2File
with bz2.BZ2File('data/sample.bz2', 'w') as f:
    f.write(b"Hello World!")

# Test BZ2File
with bz2.BZ2File('data/sample.bz2', 'a') as f:
    f.
