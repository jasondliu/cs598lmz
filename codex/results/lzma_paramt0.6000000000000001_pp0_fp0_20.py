from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_AUTO)
</code>
This works fine on Python 3.5, but fails on Python 3.6 with the error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.6/lzma.py", line 263, in __init__
    self._init_decompressor(format)
  File "/usr/lib/python3.6/lzma.py", line 271, in _init_decompressor
    self._decompressor = _decompressobj()
  File "lzmamodule.c", line 459, in _decompressobj
SystemError: NULL result without error in PyObject_Call
</code>
The code works fine on Python 3.6 if I specify the format as FORMAT_XZ, but I'd rather not require this.
Is this a bug in Python 3.6? Is there a workaround?

