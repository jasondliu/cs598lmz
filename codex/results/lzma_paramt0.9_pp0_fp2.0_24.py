from lzma import LZMADecompressor
LZMADecompressor(lzma.FORMAT_RAW, None).decompress(b'\xc0\x8b\xacOn\x7f1\x14\x8b5\x00\x00\x01\x04]\xaf\x16')
#b'AAA'
</code>
Python 3.6, 3.7, 3.8: (fails)
<code>LZMADecompressor(lzma.FORMAT_RAW, None).decompress(b'\xc0\x8b\xacOn\x7f1\x14\x8b5\x00\x00\x01\x04]\xaf\x16')
#Traceback (most recent call last):
#  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
#  File "/opt/python/3.6.9/lib/python3.6/lzma.py", line 796, in decompress
#  File "/opt/python/3.6.9/lib/python3.6/
