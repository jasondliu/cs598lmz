from lzma import LZMADecompressor
LZMADecompressor().decompress(s)
</code>
But it's not working. I get the error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.7/lzma.py", line 239, in decompress
    return self.decompressobj.decompress(data, max_length)
  File "/usr/lib/python3.7/lzma.py", line 82, in decompress
    self._buffer = self._buffer + data
TypeError: can only concatenate bytes or bytearray (not "str")
</code>
Why? How can I decompress that string?


A:

The exception message is pretty clear...
<code>TypeError: can only concatenate bytes or bytearray (not "str")
</code>
...you can only concatenate <code>bytes</code> or <code>bytearray</code> with <code>bytes</code> or <code>byt
