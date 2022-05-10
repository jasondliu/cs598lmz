import lzma
# Test LZMADecompressor
compressor = lzma.LZMADecompressor()
compressor.decompress(b'\x00')
compressor.decompress(b'\x00')
compressor.decompress(b'\x00')
compressor.decompress(b'\x00')
compressor.decompress(b'\x00')
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "C:/Users/Desktop/lzma.py", line 14, in &lt;module&gt;
    compressor.decompress(b'\x00')
  File "C:\Users\AppData\Local\Programs\Python\Python37\lib\lzma.py", line 487, in decompress
    return self._buffer_decompress(data, max_length, eof)
  File "C:\Users\AppData\Local\Programs\Python\Python37\lib\lzma.py", line 510, in _buffer_decompress
    raise LZMAError("LZMA -
