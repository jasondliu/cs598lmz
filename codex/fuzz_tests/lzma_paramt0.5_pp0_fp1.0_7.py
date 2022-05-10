from lzma import LZMADecompressor
LZMADecompressor().decompress(file)
</code>
but I get an error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "C:\Users\johndoe\AppData\Local\Programs\Python\Python38-32\lib\lzma.py", line 736, in decompress
    return self.decompress(data, max_length, False)
  File "C:\Users\johndoe\AppData\Local\Programs\Python\Python38-32\lib\lzma.py", line 727, in decompress
    return _decompress(self._decompressor, data, max_length, True)
  File "C:\Users\johndoe\AppData\Local\Programs\Python\Python38-32\lib\lzma.py", line 707, in _decompress
    raise LZMAError("Compressed data ended before the end-of-stream marker was reached")
lzma.LZMAError: Comp
