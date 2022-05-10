from bz2 import BZ2Decompressor
BZ2Decompressor()
</code>
and 
<code>from bz2 import BZ2File
BZ2File()
</code>
and 
<code>import bz2
bz2.decompress()
</code>
and
<code>import bz2
bz2.open()
</code>
and
<code>import bz2
bz2.BZ2File()
</code>
and
<code>import bz2
bz2.BZ2Decompressor()
</code>
I'm using Python 2.7.5 on a 64-bit OS X 10.9.1.


A:

You're probably looking for <code>bz2.BZ2File</code>.
<code>&gt;&gt;&gt; import bz2
&gt;&gt;&gt; bz2.BZ2File
&lt;class bz2.BZ2File at 0x10b8e3a88&gt;
</code>
This is a file-like object that allows you to read and write bzip
