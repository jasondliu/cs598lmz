from bz2 import BZ2Decompressor
BZ2Decompressor().flush()

from bz2 import compress
compress(value)

from bz2 import decompress
decompress(value)

import bz2
with bz2.BZ2File('file.bz2', 'wb') as f:
    f.write(b'hello world')

bz2.BZ2Compressor()
bz2.BZ2Decompressor()

import bz2
with bz2.open('file.bz2', 'wb') as f:
    f.write(b'hello world')
