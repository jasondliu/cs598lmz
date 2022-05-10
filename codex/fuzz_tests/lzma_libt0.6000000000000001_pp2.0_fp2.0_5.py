import lzma
lzma.LZMADecompressor()
</code>
When I am trying to import lzma module it is giving error like below
<code>Traceback (most recent call last):
  File "&lt;pyshell#0&gt;", line 1, in &lt;module&gt;
    import lzma
  File "C:\Python27\lib\lzma.py", line 10, in &lt;module&gt;
    from _lzma import *
ImportError: DLL load failed: The specified module could not be found.
</code>
I am using Windows 7 64 bit.
and Python2.7 64 bit.
Please help me how to resolve this issue.
Thanks in advance.


A:

You need to install the <code>pyliblzma</code> module on Windows.

