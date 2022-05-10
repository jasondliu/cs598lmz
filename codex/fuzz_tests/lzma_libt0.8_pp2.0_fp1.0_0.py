import lzma
lzma.open('test.xz')
</code>
But I get the error:
<code>  Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/home/tparker/anaconda3/envs/tensorflow/lib/python3.8/lzma.py", line 1205, in open
    return LZMAFile(filename, mode, **kwargs)
  File "/home/tparker/anaconda3/envs/tensorflow/lib/python3.8/lzma.py", line 1223, in __init__
    raise ValueError("streammode must be 'r', 'rb', 'w', 'wb', or None")
ValueError: streammode must be 'r', 'rb', 'w', 'wb', or None
</code>
What am I doing wrong?


A:

You can use the <code>subprocess</code> module to call the <code>xz</code> CLI driver:
<code>import subprocess
