import bz2
bz2_file = bz2.BZ2File('sample.bz2')
bz2_data = bz2_file.read()
print(bz2_data)

import lzma
xz_file = lzma.open('sample.xz')
xz_data = xz_file.read()
print(xz_data)

xz_file.close()
bz2_file.close()
gzip_file.close()

import os
os.remove('sample.gz')
os.remove('sample.bz2')
os.remove('sample.xz')
