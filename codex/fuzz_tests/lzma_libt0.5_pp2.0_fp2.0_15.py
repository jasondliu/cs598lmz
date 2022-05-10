import lzma
lzma.LZMADecompressor()
</code>
This works fine in python2, but in python3, I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.6/lzma.py", line 37, in __init__
    self.decompressor = _lzma.LZMADecompressor()
TypeError: __init__() missing 1 required positional argument: 'preset'
</code>
I can't find any documentation on this.  the lzma module is supposed to be the same in python2 and python3.  What is going on?  How do I fix this?


A:

The <code>preset</code> argument is optional in Python 2, but required in Python 3.

