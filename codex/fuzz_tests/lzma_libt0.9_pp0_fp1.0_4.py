import lzma
lzma.LZMADecompressor()
</code>
the result of the traceback is:
<blockquote>
<p>Traceback (most recent call last):   File "", line 1, in
   ModuleNotFoundError: No module named 'lzma'</p>
</blockquote>
The same python code snippet works when running with Python version 2.7.12
The error above occurs when running on Python version 3.6.6rc1
I have tried all of the commands found in this Stackoverflow question:
Unable to install lzma on Windows
Same error described above.


A:

There is no lzma module for Python 3 that is why you cannot import it.
lzma module is available for Python 2.x
There is only lzma module available for Python 3.x which can be found here
LZMA Module

