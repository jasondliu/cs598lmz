from bz2 import BZ2Decompressor
BZ2Decompressor()
</code>
But this still seems to have the same problem. The error message is:
<code>/usr/local/Cellar/python3/3.3.2/Frameworks/Python.framework/Versions/3.3/lib/python3.3/bz2.py in __init__(self)
    129         self.decompressor = _bz2.decompressor()
    130 
--&gt; 131     def decompress(self, data, size=0):
    132         """Decompress *data*, returning uncompressed data as bytes.
    133 

_bz2.error: error in bz2 decompression
</code>


A:

You're trying to open a bzip2-compressed file. Use the <code>bz2</code> module to handle them:
<code>&gt;&gt;&gt; with bz2.BZ2File("test.txt.bz2") as f:
...     print(f.read())
...     
b'This is a test.'
</code>
A <code>
