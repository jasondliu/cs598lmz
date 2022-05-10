from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(data))

# or

bz2.decompress(bz2.compress(data))
</code>

