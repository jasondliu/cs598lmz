import lzma
lzma.LZMADecompressor
</code>
which is strange. I'm importing the <code>lzma</code> module from the <code>pylzma</code> package, which is the only package I have that contains the module.
Am I doing something wrong, or is the <code>lzma</code> module really missing?
I'm using Python 3.6 on Windows 10.


A:

The <code>lzma</code> module is available in the <code>pylzma</code> package.
<blockquote>
<p>The <code>&lt;code&gt;lzma&lt;/code&gt;</code> module requires the <a href="https://pypi.python.org/pypi/pyliblzma/" rel="nofollow noreferrer">pyliblzma</a> extension module.</p>
</blockquote>

