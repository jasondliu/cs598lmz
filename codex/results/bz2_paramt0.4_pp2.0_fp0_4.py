from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('enwiki-latest-pages-articles.xml.bz2', 'rb').read())
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python2.7/bz2.py", line 224, in decompress
    return self.decompress(data)
  File "/usr/lib/python2.7/bz2.py", line 273, in decompress
    return self._buffer.read(size)
  File "/usr/lib/python2.7/bz2.py", line 524, in read
    self._fill(size)
  File "/usr/lib/python2.7/bz2.py", line 549, in _fill
    self._buffer = self._decompressor.decompress(data, size)
IOError: Invalid data stream
</code>
I am running Ubuntu 12.04 and Python 2.7.3.
Thanks for
