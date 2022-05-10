from lzma import LZMADecompressor
LZMADecompressor()
</code>
__
<blockquote>
<p><strong>Expected:</strong></p>
</blockquote>
<code>&lt;lzma.LZMADecompressor object at 0x7f6fbba086d8&gt;
</code>
<blockquote>
<p><strong>Actual:</strong></p>
</blockquote>
<code>Traceback (most recent call last):
  File "/home/dev/PycharmProjects/untitled/test.py", line 3, in &lt;module&gt;
    LZMADecompressor()
  File "/usr/lib/python3.8/lzma.py", line 56, in __init__
    self.reset()
  File "/usr/lib/python3.8/lzma.py", line 84, in reset
    self._decompressor = _lzma.LZMADecompressor()
_lzma.LZMAError: Error -1: Unknown error
</code>
На верси
