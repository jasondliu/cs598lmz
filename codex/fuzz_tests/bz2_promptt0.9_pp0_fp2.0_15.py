import bz2
# Test BZ2Decompressor
src = bz2.BZ2File(fn, buffering=0, compress=True)
src.seek(0)
for block in iter(lambda: src.read(100*1024), b''):
    dctx.decompress(block)
</code>
It's also important to note that <code>bz2.BZ2File</code> has a <code>compresslevel=9</code> option that isn't reflected with this method. So you could experiment with that as well if it makes a significant difference.

