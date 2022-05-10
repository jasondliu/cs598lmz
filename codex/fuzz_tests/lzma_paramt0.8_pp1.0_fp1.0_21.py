from lzma import LZMADecompressor
LZMADecompressor()
</code>
expected result: no errors
actual result:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python2.7/lzma.py", line 12, in __init__
    self._decompressor = _lzma.decompressobj()
_lzma.LZMAError: Input format not supported by decoder
</code>
Please help me with this.


A:

I ran into the same issue.
The problem is that you are using a x86_64 machine, which gives you the following error: 
<blockquote>
<p>_lzma.LZMAError: Input format not supported by decoder</p>
</blockquote>
When you are using a 32-bit machine, you get: 
<blockquote>
<p>NotImplementedError: This version of Python was built without XZ support</p>
</blockquote>
So my solution was to use a 32-bit machine.
