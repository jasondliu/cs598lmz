import bz2
bz2.decompress()
</code>
Get the following error
<blockquote>
<p>Traceback (most recent call last):</p>
<p>File "", line 1, in </p>
<p>AttributeError: 'module' object has no attribute 'decompress'</p>
</blockquote>
Is bz2 the wrong module to be using?  If so which one should I be using?
Thanks,


A:

You need to create a compressor object:
<code>import bz2
bz2.BZ2Decompressor().decompress()
</code>

