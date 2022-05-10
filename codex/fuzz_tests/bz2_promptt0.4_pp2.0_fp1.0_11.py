import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as fh:
    file_content = fh.read()

uncompressed_data = bz2_decompressor.decompress(file_content)

print('uncompressed_data is {} bytes'.format(len(uncompressed_data)))

uncompressed_data[:100]

# Test BZ2File

with bz2.BZ2File('data/enwik8.bz2', 'rb') as bz2_file:
    file_content = bz2_file.read()

print('file_content is {} bytes'.format(len(file_content)))

file_content[:100]

# Test BZ2File with context manager

with bz2.BZ2File('data/enwik8.bz2', 'rb') as bz2_file:
    for line in bz2_file:
        print(line)
       
