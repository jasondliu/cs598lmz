import bz2
# Test BZ2Decompressor with decompress() method

with bz2.open('example.bz2') as f:
    file_content = f.read()
    print(file_content)

decompressor = bz2.BZ2Decompressor()
uncompressed_data = decompressor.decompress(file_content)
print(uncompressed_data)

uncompressed_data = decompressor.decompress(file_content[5:])
print(uncompressed_data)

uncompressed_data = decompressor.decompress(file_content[5:15])
print(uncompressed_data)

uncompressed_data = decompressor.decompress(file_content[5:15] + file_content[30:50])
print(uncompressed_data)

uncompressed_data = decompressor.decompress(file_content[5:15] + file_content[30:50] + file_content[60:])
print(uncompressed_data)

decompressor = bz2.BZ2Decompressor()

