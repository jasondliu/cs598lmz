import lzma
lzma.LZMAFile("bz2_file.txt.bz2")
</code>
but I get:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python2.7/lzma.py", line 15, in __init__
    self._init_container(container)
  File "/usr/lib/python2.7/lzma.py", line 45, in _init_container
    raise NotImplementedError("container format not yet supported")
NotImplementedError: container format not yet supported
</code>
Is there another way to use lzma on bz2 files?


A:

I don't think there is a way to decompress a bz2 file with lzma, but you can decompress it with bz2 and then compress it with lzma.
<code>import lzma
import bz2

f_in = bz2.BZ2File("bz2_file.
