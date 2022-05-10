import bz2
bz2_file = bz2.BZ2File('data/sample.bz2')
decompressed_data = bz2_file.read()
bz2_file.close()
print(decompressed_data)

import gzip
with gzip.open('data/sample.gz', 'rb') as f:
    decompressed_data = f.read()
    print(decompressed_data)

import lzma
with lzma.open('data/sample.xz', 'rb') as f:
    decompressed_data = f.read()
    print(decompressed_data)
