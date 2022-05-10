from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# example

from bz2 import BZ2File

with BZ2File('sample.bz2') as f:
    content = f.read()
