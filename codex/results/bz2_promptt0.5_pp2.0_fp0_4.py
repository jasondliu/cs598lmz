import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Decompress with bz2
print(bz2.decompress(compressed_data))

# Decompress with context manager
with bz2.BZ2File(path, 'rb') as bz_file:
    print(bz_file.read())

# Decompress with context manager
with bz2.BZ2File(path, 'rb') as bz_file:
    for line in bz_file:
        print(line)

# Decompress with context manager
with bz2.BZ2File(path, 'rb') as bz_file:
    for line in bz_file:
        print(line.decode('utf-8'))

# Decompress with context manager
with bz2.BZ2File(path, 'rb') as bz_file:
    file_content = bz_file.read()
    file_content_decoded = file_content
