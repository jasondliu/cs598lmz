from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# or...

import gzip
with gzip.open(filename, 'rb') as f:
    f.read()
</code>

