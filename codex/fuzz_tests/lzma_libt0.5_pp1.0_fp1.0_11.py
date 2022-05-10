import lzma
lzma.decompress(data)
</code>
This produces the following error:
<code>  File "C:\Python27\lib\site-packages\lzma.py", line 55, in decompress
    return LZMADecompressor().decompress(data)
  File "C:\Python27\lib\site-packages\lzma.py", line 167, in decompress
    return self.decompressobj.decompress(data, max_length)
  File "C:\Python27\lib\site-packages\lzma.py", line 467, in decompress
    self._buffer_unused()
  File "C:\Python27\lib\site-packages\lzma.py", line 495, in _buffer_unused
    self._fill_buffer()
  File "C:\Python27\lib\site-packages\lzma.py", line 507, in _fill_buffer
    raise LZMAError("Compressed file ended before the "
lzma.LZMAError: Compressed file ended before the end-of-stream
