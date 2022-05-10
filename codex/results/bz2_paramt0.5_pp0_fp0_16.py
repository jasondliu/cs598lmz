from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.decompress(f.read(1024)))
</code>

