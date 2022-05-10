import lzma
lzma.open()
</code>
This is the error I get:
<code>Traceback (most recent call last):
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python36-32\lib\site-packages\lzma.py", line 18, in &lt;module&gt;
    from _lzma import *
ImportError: DLL load failed: The specified module could not be found.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python36-32\lib\site-packages\lzma.py", line 20, in &lt;module&gt;
    from backports.lzma import *
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python36-32\lib\site-packages\backports\lzma\__init__.py", line 8, in &lt;module&gt;
    from . import _lzma
ImportError: D
