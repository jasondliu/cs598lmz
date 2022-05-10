import lzma
lzma.open()
</code>
I get the error
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.3/lzma.py", line 25, in open
    return LZMADecompressor().decompress(data)
  File "/usr/lib/python3.3/lzma.py", line 488, in decompress
    return self.decompressobj.decompress(data)
  File "/usr/lib/python3.3/lzma.py", line 370, in decompress
    self._buffer = self._buffer + data
TypeError: can only concatenate str (not "bytes") to str
</code>
I've tried to find a solution but I don't understand what the problem is here.


A:

<code>lzma.open()</code> is a convenience wrapper around the <code>lzma.LZMADecompressor</code> class. The <code
