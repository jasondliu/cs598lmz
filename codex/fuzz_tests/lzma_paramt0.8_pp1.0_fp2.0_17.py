from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
</code>
But I get this error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lzma.py", line 563, in decompress
    return self.decompress(data, max_length, max_length)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lzma.py", line 554, in decompress
    return self.decompress(data, max_length, max_length)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lzma.py", line 545, in decompress
    return self.decompress_chunk(data, max_length)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lzma.py",
