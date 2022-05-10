import lzma
lzma.LZMA_FILTER_ARM
</code>
It is returning an error.
<code>---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
&lt;ipython-input-7-8a1c6d7f6a9d&gt; in &lt;module&gt;
----&gt; 1 lzma.LZMA_FILTER_ARM

AttributeError: module 'lzma' has no attribute 'LZMA_FILTER_ARM'
</code>
How can I fix it?


A:

Try <code>lzma.FILTER_ARM</code> instead.

