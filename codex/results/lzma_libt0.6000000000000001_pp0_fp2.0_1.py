import lzma
lzma.decompress(data)
</code>
but I am getting the following error:
<code>Traceback (most recent call last):
File "&lt;stdin&gt;", line 1, in &lt;module&gt;
File "/usr/lib/python3.6/lzma.py", line 14, in decompress
return LZMADecompressor(format=FORMAT_RAW, check=-1).decompress(data)
File "/usr/lib/python3.6/lzma.py", line 673, in decompress
self.eof = self._decompressor.decompress(data, size)
File "/usr/lib/python3.6/lzma.py", line 458, in decompress
return self.decompressor.decompress(data, available_size)
ValueError: Data is not LZMA-compressed
</code>
I have tried using the <code>xz</code> library too, but I am getting the same error.
Any ideas?

