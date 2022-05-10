from lzma import LZMADecompressor
LZMADecompressor()
</code>
But when I try to run the script from the command line, this error occurs
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    LZMADecompressor()
  File "/usr/local/python3/lib/python3.8/site-packages/lzma.py", line 13, in __init__
    _decompressobj.__init__(self, format=FORMAT_XZ, check=-1)
AttributeError: module 'lzma' has no attribute 'FORMAT_XZ'
</code>
I have installed the liblzma-dev package, what else should I install?


A:

I have the same problem and I have fixed it.
I use <code>pipenv</code> to manage my virtual environment, and the problem is caused by incompatible versions between <code>pylzma</code> and <code>lzma</code>.
The solution is:
<code>pipenv install --skip-lock lzma
</code>
