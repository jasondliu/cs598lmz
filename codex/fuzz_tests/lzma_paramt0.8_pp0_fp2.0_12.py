from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00').decode('utf-8')

# OUTPUT: hello
</code>
Works in Python3.5 and Python3.6, but fails in 3.7 and up.
<code># in Python3.7
&gt;&gt;&gt; from lzma import LZMADecompressor
&gt;&gt;&gt; LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00').decode('utf-8')
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.7/lzma.py", line 247, in decompress
    return self.decompressobj.decompress(data, max_length)
  File "/usr/lib/python3.7/lzma.py", line 275, in decompress
