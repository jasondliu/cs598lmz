from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.BZ2File('data.bz2').read())

# or

with bz2.BZ2File('data.bz2') as f:
    data = f.read()

# or

import bz2
with open('data.bz2', 'rb') as f:
    data = bz2.decompress(f.read())
</code>

