import lzma
lzma.LZMAError:
  File "/usr/lib/python3.6/lzma.py", line 21, in &lt;module&gt;
    from _lzma import *
ImportError: /usr/lib/python3.6/lib-dynload/_lzma.cpython-36m-x86_64-linux-gnu.so: undefined symbol: PyUnicodeUCS4_AsASCIIString
</code>
I tried to install <code>liblzma-dev</code> but it didn't help.
I'm using Ubuntu 18.04.

