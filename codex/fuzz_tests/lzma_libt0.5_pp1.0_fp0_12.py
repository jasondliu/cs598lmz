import lzma
lzma.open()
</code>
But I am getting the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.5/lzma.py", line 8, in &lt;module&gt;
    from _lzma import *
ImportError: /usr/lib/python3.5/lib-dynload/_lzma.cpython-35m-x86_64-linux-gnu.so: undefined symbol: PyUnicodeUCS2_AsUTF8String
</code>
How can I fix this?

