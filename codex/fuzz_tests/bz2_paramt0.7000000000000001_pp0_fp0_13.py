from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b)
</code>
The only downside of this is that you're using memory for the compressed and uncompressed data, but it doesn't really matter.

