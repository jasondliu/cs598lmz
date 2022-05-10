from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open("/tmp/enwiki-latest-pages-articles.xml.bz2").read(100))
</code>
This is the error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/local/Cellar/python/2.7.10_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/bz2.py", line 242, in decompress
    return self.decompress(data)
  File "/usr/local/Cellar/python/2.7.10_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/bz2.py", line 230, in decompress
    self._buffer = self._buffer + data
MemoryError
</code>
I am not sure why it's complaining about memory. I have 8GB of RAM.
I am running OSX 10.11.4 with the latest version of Python.

