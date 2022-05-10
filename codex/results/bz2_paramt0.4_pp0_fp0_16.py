from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('/home/dave/Downloads/enwiki-latest-pages-articles.xml.bz2', 'rb').read())
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python2.7/bz2.py", line 220, in decompress
    return self.decompress(data).decode('iso-8859-1')
  File "/usr/lib/python2.7/bz2.py", line 228, in decompress
    self._buffer = self._buffer + data
MemoryError
</code>
I have a lot of memory available, and I can't figure out why I'm getting this error.
I'm running Ubuntu 12.04 on a 64-bit machine with 16 GB of RAM.


A:

The decompressed size of the file is more than 16GB. You will need to decompress the file in chunks.

