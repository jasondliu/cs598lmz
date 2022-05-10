from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# zlib
import zlib
zlib.decompress(data)

import bz2, gzip
with bz2.open('example.bz2', 'rb') as bz_input:
    with gzip.open('example.gz', 'wb') as gz_output:
        gz_output.write(bz_input.read())

# 将一个文件解压到另一个文件
import bz2
f_in = bz2.open('example.bz2', 'rb')
f_out = gzip.open('example.gz', 'wb')
f_out.write(f_in.read())
f_out.close()
f_in.close()
