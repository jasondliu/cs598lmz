from bz2 import BZ2Decompressor
BZ2Decompressor()
</code>
Output:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/local/lib/python2.7/bz2.py", line 24, in &lt;module&gt;
    from _bz2 import BZ2Compressor, BZ2Decompressor
ImportError: No module named _bz2
</code>
I'm not sure what I'm missing here.
Thanks.


A:

This is a bug in the Python 2.7.6 installer. See this bug report for details.

