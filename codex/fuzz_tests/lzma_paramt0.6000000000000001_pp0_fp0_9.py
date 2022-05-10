from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
</code>
which gives the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.5/lzma.py", line 557, in decompress
    return self.decompressor.decompress(data, max_length)
  File "/usr/lib/python3.5/lzma.py", line 382, in decompress
    return self._buffer_decompress(data, max_length)
  File "/usr/lib/python3.5/lzma.py", line 394, in _buffer_decompress
    return self._decompressor.decompress(data, max_length)
  File "/usr/lib/python3.5/lzma.py", line 252, in decompress
    self._check_can_decompress()
  File "/usr/lib/python3.5/lzma.py", line 242, in _check_can
