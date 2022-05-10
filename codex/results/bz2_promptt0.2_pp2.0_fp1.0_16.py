import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('sample.bz2', 'rb') as f:
    file_content = f.read()

uncompressed_data = decompressor.decompress(file_content)

print(uncompressed_data)

# Test BZ2File

with bz2.BZ2File('sample.bz2', 'rb') as f:
    file_content = f.read()

print(file_content)

# Test BZ2File with context manager

with bz2.BZ2File('sample.bz2', 'rb') as f:
    for line in f:
        print(line)

# Test BZ2File with context manager

with bz2.BZ2File('sample.bz2', 'rb') as f_in, open('sample.txt', 'wb') as f_out:
    f_out.write(f_in.read())

# Test BZ2File with context manager

with bz2.BZ
