from lzma import LZMADecompressor
LZMADecompressor()
</code>
The error message is:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/local/lib/python3.5/dist-packages/lzma/__init__.py", line 17, in __init__
    self._decompressor = _lzma.LZMADecompressor(format=format, memlimit=memlimit, filters=filters)
ValueError: unsupported format
</code>
I'm using Ubuntu 16.04 LTS and Python 3.5.2. 
How can I solve this problem?


A:

You need to upgrade your <code>pyliblzma</code> package to version <code>0.5.3-4</code> or later. 
It seems that your <code>pyliblzma</code> was built against an older version of liblzma (XZ Utils) which does not support the <code>xz</code> format.

