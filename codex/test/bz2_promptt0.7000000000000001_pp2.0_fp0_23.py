import bz2
# Test BZ2Decompressor with decompress() method

with bz2.open('example.bz2') as f:
    file_content = f.read()
    print(file_content)

decompressor = bz2.BZ2Decompressor()
uncompressed_data = decompressor.decompress(file_content)
print(uncompressed_data)

