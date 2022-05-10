from lzma import LZMADecompressor
LZMADecompressor().decompress(FILE_COMPRESSED)
</code>
But this results in the following error:
<code>
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "C:\Users\User\AppData\Local\Programs\Python\Python38-32\lib\lzma.py", line 264, in decompress
self._buffer_unused()
  File "C:\Users\User\AppData\Local\Programs\Python\Python38-32\lib\lzma.py", line 297, in _buffer_unused
raise LZMAError("unconsumed data remains")
lzma.LZMAError: unconsumed data remains
</code>
Could anyone help me with this issue? I'm really new to Python and to XZ format.
Thanks in advance!


A:

LZMA compressors have a notion of a "stream" which is basically a single file, or portion of a file that has been compressed.  The last few bytes of this stream contain a checksum and some other metadata.  This is done so that a
