import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()
compressed = lzma.compress(b'Hello world')
decomp.decompress(compressed)

'Hello world'

decomp.decompress(compressed)

''

decomp.decompress(compressed)

Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python2.7/lzma.py", line 234, in decompress
    return self.decompressobj.decompress(data)
  File "/usr/lib/python2.7/lzma.py", line 307, in decompress
    raise LZMAError("LZMA error: Input format not recognized")
lzma.LZMAError: LZMA error: Input format not recognized
</code>
I found the issue is that <code>lzma</code> only supports one stream per LZMADecompressor instance. So when you call <code>dec
