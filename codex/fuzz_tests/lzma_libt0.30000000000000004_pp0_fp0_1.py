import lzma
lzma.decompress(data)
</code>
But I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "C:\Python27\lib\site-packages\lzma.py", line 489, in decompress
    return _decompress(data, format, memlimit, filters)
  File "C:\Python27\lib\site-packages\lzma.py", line 468, in _decompress
    return _decompress_buf(data, format, memlimit, filters)
  File "C:\Python27\lib\site-packages\lzma.py", line 456, in _decompress_buf
    return _decompress_buf_safe(data, format, memlimit, filters)
  File "C:\Python27\lib\site-packages\lzma.py", line 446, in _decompress_buf_safe
    return _decompress_buf_unsafe(data, format,
