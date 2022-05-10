import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    file_content = f.read()

decompressed_data = decompressor.decompress(file_content)

print(len(decompressed_data))

with open('data/enwik8_decompressed', 'wb') as f:
    f.write(decompressed_data)

# Test BZ2File

with bz2.BZ2File('data/enwik8.bz2', 'rb') as f:
    file_content = f.read()

print(len(file_content))

with open('data/enwik8_decompressed_2', 'wb') as f:
    f.write(file_content)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/enwik8_decompressed', 'rb') as f:
    file_content = f.read()
