from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
</code>
However, I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.5/lzma.py", line 273, in decompress
    return b''.join(_buffer_decompress(self, [data]))
  File "/usr/lib/python3.5/lzma.py", line 337, in _buffer_decompress
    data = comp.decompress(data)
  File "/usr/lib/python3.5/lzma.py", line 238, in decompress
    return self.decompressor.decompress(data)
  File "/usr/lib/python3.5/lzma.py", line 511, in decompress
    return _decompress(self._buffer, data, self.unconsumed_tail, self._eof)
lzma.LZMAError: Input format not supported by decoder
</code>
