from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'1')
'1'

&gt;&gt;&gt; import bz2
bz2.BZ2Decompressor().decompress(b'1')
'1'

&gt;&gt;&gt; bz2.decompress(b'1')
'1'

&gt;&gt;&gt; from bz2 import decompress
decompress(b'1')
'1'

&gt;&gt;&gt; import bz2
bz2.decompress(b'1')
'1'
</code>
...as you can see, you have a "duplicate function"
<code>&gt;&gt;&gt; print(bz2.decompress)
&lt;built-in function decompress&gt;
&gt;&gt;&gt; print(decompress)
&lt;function decompress at 0x7f8eb0efb2f0&gt;
</code>
...and the import of the module overrides the built-in

