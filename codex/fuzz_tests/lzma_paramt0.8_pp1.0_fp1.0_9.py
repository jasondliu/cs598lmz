from lzma import LZMADecompressor
LZMADecompressor()
</code>
It works without error on Unix, and works on Windows in the standard shell. But when I run it in Windows Subsystem for Linux (<code>WSL</code>), this error occurs:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.6/lzma.py", line 23, in __init__
    bufsize=bufsize, check=-1)
OSError: [Errno 22] Invalid argument
</code>
I am wondering what is wrong.
PS: I found that if I use <code>import lzma</code> in <code>Python</code> shell instead of <code>import lzma</code> in <code>IPython</code>, the problem doesn't occur. But I don't know what's the relationship between the problem and <code>IPython</code>.

