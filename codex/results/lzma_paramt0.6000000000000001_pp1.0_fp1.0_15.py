from lzma import LZMADecompressor
LZMADecompressor().decompress(s)
</code>
This is the truncated error message:
<code>Traceback (most recent call last):
  File "C:\Program Files\Python35\lib\site-packages\lzma.py", line 521, in decompress
    return self.decompressobj.decompress(data)
  File "C:\Program Files\Python35\lib\site-packages\lzma.py", line 307, in decompress
    return _decompress(self._decompressor, data, max_length, _buffer)
  File "C:\Program Files\Python35\lib\site-packages\lzma.py", line 271, in _decompress
    return func(data, buf_size, out)
  File "C:\Program Files\Python35\lib\site-packages\lzma.py", line 221, in _decompressBuffer
    ret = _decompress_buf(self._decompressor, data, buf_size, out)
  File "C:\Program Files\Python35\lib\site-packages\lz
