from bz2 import BZ2Decompressor
BZ2Decompressor()
</code>
This works fine in Python 2.7, but in Python 3.3 the following error is shown:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: object.__new__() takes no parameters
</code>
I'm not sure what it means.

