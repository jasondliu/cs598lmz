import lzma
lzma.open()
</code>
This works fine on my Mac, but when I try to run it on Windows, I get the following error:
<code>Traceback (most recent call last):
  File "C:\Users\User\Desktop\test.py", line 3, in &lt;module&gt;
    lzma.open()
  File "C:\Python27\lib\lzma.py", line 11, in open
    return LZMAFile(filename, mode, **kwargs)
  File "C:\Python27\lib\lzma.py", line 49, in __init__
    self._init_stream(flags)
  File "C:\Python27\lib\lzma.py", line 56, in _init_stream
    self._stream = _lzma.LZMAStream(**kwargs)
TypeError: __init__() got an unexpected keyword argument 'preset'
</code>
I know that the file is not corrupted, as I can open it using 7-zip on Windows.
I am using Python version 2.7.12 on Windows.

