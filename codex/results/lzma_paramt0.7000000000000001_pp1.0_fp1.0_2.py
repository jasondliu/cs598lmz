from lzma import LZMADecompressor
LZMADecompressor()
</code>
returns
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.5/lzma.py", line 67, in __init__
    self._init_decompress_state(lzma._decompress_reset)
  File "/usr/lib/python3.5/lzma.py", line 112, in _init_decompress_state
    self._decompress = self._decompress_func(self._decompress_state)
lzma.LZMAError: Initialization error: Memory allocation failed
</code>
I suspect it is because I am running Ubuntu 16.04 on Digital Ocean with only 512MB of memory, which is too little, but I don't know how to prove that.


A:

I was able to solve the issue by increasing my memory to 1GB. The 512MB was too little.

