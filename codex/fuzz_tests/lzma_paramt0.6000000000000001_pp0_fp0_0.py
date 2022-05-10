from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_ALONE, memlimit=1 * 1024 * 1024 * 1024)
</code>
I get the error
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.7/lzma.py", line 300, in __init__
    super().__init__()
  File "/usr/lib/python3.7/lzma.py", line 140, in __init__
    self._decompressor = self._decompressor_factory()
lzma.LZMAError: Invalid allocation size
</code>
It works if I call it with <code>memlimit=None</code>.
I would like to understand this behavior better. 

Is this a bug? 
Is there a way to get the uncompressed size of the file without decompressing it?
Is there a way to decompress the file without specifying <code>memlimit</code>?


