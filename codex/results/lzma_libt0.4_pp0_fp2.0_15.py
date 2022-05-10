import lzma
lzma.LZMAFile
</code>
The error message is:
<code>Traceback (most recent call last):
  File "&lt;pyshell#0&gt;", line 1, in &lt;module&gt;
    import lzma
  File "C:\Python34\lib\lzma.py", line 9, in &lt;module&gt;
    raise ImportError("No module named '_lzma'")
ImportError: No module named '_lzma'
</code>
I have tried to find a solution for this, but I can't find any. I have installed the pylzma module, but it doesn't work either. 
I am using Python 3.4.1. 
Thank you in advance.


A:

The <code>lzma</code> module is only available in Python 3.3 and above.

