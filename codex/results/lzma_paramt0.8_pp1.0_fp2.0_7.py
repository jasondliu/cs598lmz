from lzma import LZMADecompressor
LZMADecompressor().decompress(b''.join(l'[0:2]))
</code>
But when I run this code I get error:
<code>Traceback (most recent call last):
  File "C:/Users/Germus/Documents/GitHub/3_Parse_LZMA/Parse_lzma/Parse_lzma.py", line 31, in &lt;module&gt;
    LZMADecompressor().decompress(b''.join(l[0:2]))
  File "C:\Python\Python38\lib\lzma.py", line 196, in decompress
    return self.decompressobj.decompress(data)
  File "C:\Python\Python38\lib\lzma.py", line 259, in decompress
    return _decompress(self, data, max_length, _buffer_decompress)
lzma.LZMAError: Input format not supported by decoder
</code>
How I can fix it?


A:

I solve this problem. I needed to decode
