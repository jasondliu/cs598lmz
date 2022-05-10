from lzma import LZMADecompressor
LZMADecompressor()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.5/lzma.py", line 8, in &lt;module&gt;
    from _lzma import *
ImportError: No module named '_lzma'
</code>
I have tried installing <code>lzma</code> using <code>pip3</code> and <code>pip</code> without success.


A:

I had the same problem, and I solved it by installing the <code>liblzma-dev</code> package:
<code>apt-get install liblzma-dev
</code>

