import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

# Decompress a single file
with open('data/data_bz2/enwiki-latest-pages-articles1.xml-p10p30302.bz2', 'rb') as file:
    for data in iter(lambda: file.read(100 * 1024), b''):
        print(decompressor.decompress(data))

# Decompress a bunch of files

import os

dir_name = 'data/data_bz2'

for file_name in os.listdir(dir_name):
    file_path = os.path.join(dir_name, file_name)
    with open(file_path, 'rb') as file:
        for data in iter(lambda: file.read(100 * 1024), b''):
            print(decompressor.decompress(data))

# Decompress a bunch of files in a memory-efficient way

import os

dir_name = 'data/data_bz2'

for file_name in
