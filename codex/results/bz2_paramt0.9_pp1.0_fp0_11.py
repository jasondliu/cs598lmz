from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(buf)
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/home/aleksejs/.local/lib/python3.7/site-packages/bz2.py", line 264, in decompress
    return self._decompress(data)
  File "/usr/lib/python3.7/bz2.py", line 257, in _decompress
    return self._buffer.decompress(data)
  File "/home/aleksejs/work/bzip/bzdecompressor.py", line 153, in decompress
    block = self.decompress_block(block)
  File "/home/aleksejs/work/bzip/bzdecompressor.py", line 64, in decompress_block
    _rotate(self.H, self.v1, (self.v1 + self.v2) % 256)
  File "/home/aleksejs/work/bzip/bzdecompressor.py
