import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content)

decompressed_data = decompressor.decompress(file_content)
print(decompressed_data)

decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as f:
    for data in iter(lambda: f.read(100), b''):
        print(data)
        decompressed_data = decompressor.decompress(data)
        if decompressed_data:
            print(decompressed_data)

# Test BZ2File

with bz2.BZ2File('data/sample.bz2') as f:
    file_content = f.read()
    print(file_content)

with bz2.BZ2File('data/sample.bz2', 'r') as f:
    file_content
