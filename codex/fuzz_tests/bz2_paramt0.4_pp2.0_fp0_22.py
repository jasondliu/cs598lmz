from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.decompress(data))
</code>
Note that the <code>decompress()</code> method of the <code>bz2.BZ2Decompressor</code> class returns a <code>bytes</code> object.

