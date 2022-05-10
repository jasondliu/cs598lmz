from bz2 import BZ2Decompressor
BZ2Decompressor()
</code>
Which gives me the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/local/lib/python2.7/bz2.py", line 105, in __init__
    self._decompressor = _bz2.decompressor(**kwargs)
SystemError: new style getargs format but argument is not a tuple
</code>
I am a bit at a loss as to why this is so, as this is the way to initialize a BZ2Decompressor as per the examples I've seen.

