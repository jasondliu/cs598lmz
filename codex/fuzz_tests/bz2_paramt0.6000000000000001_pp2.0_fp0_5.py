from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(s)
</code>
which would be a bit more robust, but still not foolproof, as your file could contain both compressed and uncompressed data.

