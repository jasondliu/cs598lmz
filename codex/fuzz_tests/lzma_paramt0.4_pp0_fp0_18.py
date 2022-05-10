from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
</code>
However, I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.6/lzma.py", line 544, in decompress
    return self.decompressobj.decompress(data)
  File "/usr/lib/python3.6/lzma.py", line 287, in decompress
    self._buffer_unconsumed()
  File "/usr/lib/python3.6/lzma.py", line 268, in _buffer_unconsumed
    self._check_unused_data()
  File "/usr/lib/python3.6/lzma.py", line 254, in _check_unused_data
    raise LZMAError("Compressed data ended before the end-of-stream "
lzma.LZMAError: Compressed data ended before the end-of-stream marker was reached
</code>
I'm not
