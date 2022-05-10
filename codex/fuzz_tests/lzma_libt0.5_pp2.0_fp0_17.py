import lzma
lzma.open('test.tar.xz')
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.6/lzma.py", line 4, in open
    return LZMAFile(filename, mode, **kwargs)
  File "/usr/lib/python3.6/lzma.py", line 137, in __init__
    self._init_write(format)
  File "/usr/lib/python3.6/lzma.py", line 164, in _init_write
    self._check_can_write(format)
  File "/usr/lib/python3.6/lzma.py", line 199, in _check_can_write
    raise ValueError("can't specify format=%r with mode=%r" % (format, self.mode))
ValueError: can't specify format=None with mode='wb'
</code>
What is wrong?


