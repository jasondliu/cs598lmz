from bz2 import BZ2Decompressor
BZ2Decompressor(bz2.decompress(f.read()))
</code>
Moreover, if it is a <code>.bz2</code> file, why can't I just use <code>bz2.open</code>?


A:

Found a temporary solution.
<code>s = bz2.decompress(f.read())
s = s.decode('big5')
</code>
Then I can use <code>s</code> to do whatever I want.

