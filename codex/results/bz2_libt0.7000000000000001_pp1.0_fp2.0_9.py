import bz2
bz2.decompress(data)

import zlib
zlib.decompress(data)

import gzip
f = gzip.open('file.txt.gz', 'rb')
file_content = f.read()
f.close()
