import bz2
bz2.decompress(bz2.compress(b'hello world'))

from bz2 import BZ2File
with BZ2File('bz2file.bz2', 'w') as f:
    f.write(b'hello world')
with BZ2File('bz2file.bz2', 'r') as f:
    f.read()

import pprint
import bz2
from bz2 import BZ2Decompressor
dec = BZ2Decompressor()
dec.decompress(bz2.compress(b'hello world'))

from bz2 import BZ2File
from io import BytesIO
bzf = BZ2File('bz2file.bz2')
bzf.read(1)
bzf.seek(0)
bzf.readline()
bzf.seek(0)
bzf.readlines()
bzf.seek(0)
bzf.seek(0, 2)
bzf.seek(0)
bzf
