from bz2 import BZ2Decompressor
BZ2Decompressor()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python2.7/bz2.py", line 24, in __init__
    self._decompressor = _bz2.BZ2Decompressor()
bz2.BZ2Error: BZ2_bzDecompressInit: out of memory
</code>
I'm using Python 2.7.9, Ubuntu 14.04.

