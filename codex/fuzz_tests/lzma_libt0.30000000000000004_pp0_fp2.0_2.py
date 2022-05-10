import lzma
lzma.LZMACompressor()
</code>
But I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "C:\Python34\lib\lzma.py", line 58, in __init__
    self._init_compressor(preset)
  File "C:\Python34\lib\lzma.py", line 97, in _init_compressor
    self._compressor = _lzma.LZMACompressor(**kwargs)
  File "C:\Python34\lib\lzma.py", line 60, in __init__
    raise ValueError("preset must be in 0..9")
ValueError: preset must be in 0..9
</code>
I've tried to install the pylzma module, but I get the same error.
I'm using Python 3.4.1 on Windows 7.


A:

You need to pass a preset value to the constructor:
<code>lzma.L
