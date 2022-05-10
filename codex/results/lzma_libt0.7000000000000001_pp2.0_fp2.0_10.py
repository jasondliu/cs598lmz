import lzma
lzma.LZMAFile(fileobj=f)
</code>
This is the error I get:
<code>Traceback (most recent call last):
  File "lzma.py", line 6, in &lt;module&gt;
    lzma.LZMAFile(fileobj=f)
  File "/usr/lib/python2.7/lzma.py", line 75, in __init__
    self._init_decompressor(format)
  File "/usr/lib/python2.7/lzma.py", line 83, in _init_decompressor
    self._decompressor = LZMADecompressor(format)
  File "/usr/lib/python2.7/lzma.py", line 116, in __init__
    self._decompressor = lzma.decompressobj()
  File "/usr/lib/python2.7/lzma.py", line 144, in decompressobj
    return _lzma.decompressobj(*args, **kwargs)
LZMAError: Input format
