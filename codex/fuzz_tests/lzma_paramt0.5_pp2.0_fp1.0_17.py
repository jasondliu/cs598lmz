from lzma import LZMADecompressor
LZMADecompressor.__init__
</code>
but it gives me the following error:
<code>TypeError: __init__() takes 1 positional argument but 2 were given
</code>
I am using Python 3.6.2 on Windows.


A:

You don't need to instantiate the <code>LZMADecompressor</code> class. It has a <code>decompress</code> method that can be used directly.
<code>&gt;&gt;&gt; from lzma import LZMADecompressor
&gt;&gt;&gt; LZMADecompressor.decompress
&lt;method 'decompress' of 'lzma.LZMADecompressor' objects&gt;
</code>

