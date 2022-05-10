import lzma
lzma.LZMAError:
  File "/usr/lib/python3.6/lzma.py", line 10, in &lt;module&gt;
    from _lzma import *
ImportError: /usr/lib/python3.6/lib-dynload/_lzma.cpython-36m-x86_64-linux-gnu.so: undefined symbol: PyUnicodeUCS4_FromEncodedObject
</code>
I tried to install the package liblzma-dev, but it didn't work, so I decided to install the package python3-lzma, and it worked.

