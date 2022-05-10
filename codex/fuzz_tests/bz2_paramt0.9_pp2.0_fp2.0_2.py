from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open(BZ2_FILENAME).read())

</code>
The docstring for <code>bz2.open</code> says that you can also pass a <code>buffering</code> parameter with a value of <code>0</code>.
You could also just use <code>bz2.decompress</code> directly:
<code>open_file = open(BZ2_FILENAME)
bz2.decompress(open_file)
</code>

