import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

with open('sample.bz2', 'rb') as f:
    file_content = f.read()
    data = decompressor.decompress(file_content)
    print(data)

# Test BZ2File
with bz2.BZ2File('sample.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content)

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
with open('sample.bz2', 'wb') as f:
    for data in ['Hello', 'World']:
        f.write(compressor.compress(data))
    f.write(compressor.flush())

# Test BZ2File
with bz2.BZ2File('sample.bz2', 'wb') as f:
    f.write('Hello')
    f.write('World')

# Test BZ2File
with bz2.BZ2File('sample
