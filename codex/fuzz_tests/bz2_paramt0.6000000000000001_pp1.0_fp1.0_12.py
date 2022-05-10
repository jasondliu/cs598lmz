from bz2 import BZ2Decompressor
BZ2Decompressor()
</code>
<blockquote>
<p>AttributeError: module 'bz2' has no attribute 'BZ2Decompressor'</p>
</blockquote>
I have already tried:

Reinstalling <code>bz2</code> module
Reinstalling <code>gensim</code>

I have also tried:
<code>&gt;&gt;&gt; import bz2
&gt;&gt;&gt; dir(bz2)
['BZ2Compressor', 'BZ2Decompressor', 'BZ2File', 'BZ2Filter', 'BZ2Compressor', 'BZ2Decompressor', 'BZ2File', 'BZ2Filter', 'BZ2Compressor', 'BZ2Decompressor', 'BZ2File', 'BZ2Filter', 'BZ2Compressor', 'BZ2Decompressor', 'BZ2File', 'BZ2Filter', 'BZ2Compressor', 'BZ2Decompressor', 'BZ2File', 'BZ2Filter', 'BZ2
