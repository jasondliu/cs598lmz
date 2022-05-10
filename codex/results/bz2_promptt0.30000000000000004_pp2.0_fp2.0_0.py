import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    file_content = f.read()
    print(len(file_content))
    print(file_content[:10])

decompressed_data = decompressor.decompress(file_content)
print(len(decompressed_data))
print(decompressed_data[:10])

with open('data/enwik8.bz2', 'rb') as f:
    file_content = f.read()
    print(len(file_content))
    print(file_content[:10])

decompressed_data = decompressor.decompress(file_content)
print(len(decompressed_data))
print(decompressed_data[:10])

with open('data/enwik8.bz2', 'rb') as f:
    file_content = f.read()
    print(len(file_content))
    print(file_content[:10
