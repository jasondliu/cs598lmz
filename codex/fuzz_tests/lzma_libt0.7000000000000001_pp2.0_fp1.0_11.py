import lzma
lzma.LZMACompressor
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: module 'lzma' has no attribute 'LZMACompressor'
</code>
Here is the python interpreter version:
<code>Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
</code>
Here is the lzma module version:
<code>import lzma
lzma.__version__
'0.0.8'
</code>
I've tried to upgrade the module using <code>pip install --upgrade lzma</code> but it doesn't solve the problem.
How can I make it work properly?


A:

The <code>lzma</code> module which you've imported is a backport from the Python 3.3+ <code>lzma</code> module, which does not have that attribute.
If you
