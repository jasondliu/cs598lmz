import bz2
bz2.BZ2File('file.bz2')
# bz2.BZ2File('file.bz2', 'w')
# bz2.BZ2File('file.bz2', 'w', compresslevel=9)

# compress
with open('file.txt', 'rb') as src:
    data = src.read()
    with bz2.open('file.bz2', 'wb') as dst:
        dst.write(data)

# decompress
with bz2.open('file.bz2', 'rb') as src:
    data = src.read()
    with open('file.txt', 'wb') as dst:
        dst.write(data)

import gzip
gzip.open('file.gz')
# gzip.open('file.gz', 'w')
# gzip.open('file.gz', 'w', compresslevel=9)

# compress
with open('file.txt', 'rb') as src:
    data = src.read()
    with gzip.open('file.gz', '
