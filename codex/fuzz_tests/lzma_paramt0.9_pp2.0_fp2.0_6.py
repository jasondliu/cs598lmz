from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

Traceback (most recent call last):
File "&lt;stdin&gt;", line 1, in &lt;module&gt;
File "/usr/lib/python2.7/lzma.py", line 230, in decompress
return LZMADecompressor().decompress(data)
File "/usr/lib/python2.7/lzma.py", line 204, in decompress
self._buffer += self._decompressor.decompress(data, sizehint)
error: Error -5 while decompressing data: incomplete or truncated stream
</code>
How do I decompress it?


A:

Your decompression algorithm is giving you <code>b"\xfd7zb\x00\x04\x00\x00\x00\x00\x00\x00-\x99\x9a\xec\xd4\xdc\xdb\xf2\xcf\x01"</code> in <code>data</code>, not <code>b'\xfd7zXZ\
