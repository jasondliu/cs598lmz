from bz2 import BZ2Decompressor
BZ2Decompressor(data).decompress(data)
</code>
But I get the error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python2.7/bz2.py", line 159, in decompress
    return self.decompress(data)
  File "/usr/lib/python2.7/bz2.py", line 123, in decompress
    return self._decompress(data)
  File "/usr/lib/python2.7/bz2.py", line 133, in _decompress
    self.eof = True
  File "/usr/lib/python2.7/bz2.py", line 103, in _decompress
    self.decompressor.decompress(data)
  File "/usr/lib/python2.7/bz2.py", line 109, in decompress
    return self.decompress(data)
  File "/usr/lib/python2.7/bz
