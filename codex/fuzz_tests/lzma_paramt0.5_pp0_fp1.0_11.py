from lzma import LZMADecompressor
LZMADecompressor().decompress(b'')
</code>
This is the output
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.8/lzma.py", line 299, in decompress
    return self._buffer_decompress(data, maxlength, eof)
  File "/usr/lib/python3.8/lzma.py", line 356, in _buffer_decompress
    raise LZMAError("LZMA - Not enough data to decompress")
lzma.LZMAError: LZMA - Not enough data to decompress
</code>
I am using python 3.8.2 on Debian 10.

