from lzma import LZMADecompressor
LZMADecompressor()
</code>
This gives me the following error:
<code>Traceback (most recent call last):
  File "&lt;pyshell#5&gt;", line 1, in &lt;module&gt;
    LZMADecompressor()
  File "C:\Python27\lib\lzma.py", line 11, in __init__
    self._decompressor = _lzma.decompressobj()
AttributeError: 'module' object has no attribute 'decompressobj'
</code>
I am using Python 2.7.3 and the latest version of pyliblzma which I got from here.
I have tried uninstalling and reinstalling pyliblzma, but it didn't work. I have also tried installing the LZMADecompressor from the command-line, but it says that it is already installed.
I am using Windows 7.
Thanks.


A:

I had the same problem. I found out that the problem is that the pyliblzma library is not compiled for your version of python. Try installing the pyliblz
