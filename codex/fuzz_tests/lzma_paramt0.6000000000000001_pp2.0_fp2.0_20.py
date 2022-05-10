from lzma import LZMADecompressor
LZMADecompressor()
</code>
However, when I run it, I get the following error:
<code>AttributeError: 'module' object has no attribute 'decompress'
</code>
I am using IPython version 3.1.0, with Python 3.4.3 on OS X 10.10.4. I tried using Python 2.7.10, but I get the same error.
I can do <code>import lzma</code> without any issues. Any ideas on how to fix this?
Edit: I've tried <code>pip install backports.lzma</code>, and I get the same error.


A:

<code>lzma</code> is included in the standard library, but <code>backports.lzma</code> is a backport of the <code>lzma</code> module which is new in Python 3.3. So, if you're using Python 3.3 or newer, you don't need to install anything; if you're using an older version of Python, you can install the <code>backports.lzma</code> package.

