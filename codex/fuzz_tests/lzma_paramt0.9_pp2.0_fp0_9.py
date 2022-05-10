from lzma import LZMADecompressor
LZMADecompressor().decompress(doc)
</code>
still gives me 
<code>Traceback (most recent call last):
  File "&lt;pyshell#3&gt;", line 1, in &lt;module&gt;
    LZMADecompressor().decompress(doc)
  File "C:\Python\lib\lzma.py", line 287, in decompress
    return self.decompress_buffer(data, size)
  File "C:\Python\lib\lzma.py", line 273, in decompress_buffer
    data = self._decompressobj.decompress(data, size)
  File "C:\Python\lib\lzma.py", line 255, in _check_size
    raise LZMAError("did not provide enough data")
lzma.LZMAError: did not provide enough data
</code>
and the bytes of the document itself:
<code>b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1\x00\x00\
