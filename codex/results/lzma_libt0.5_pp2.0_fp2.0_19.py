import lzma
lzma.decompress(data)
</code>
I get the following error:
<code>lzma.error: Error -3 while decompressing data: invalid distance too far back
</code>
I'm not sure what is wrong, as I'm passing it a byte string, and it should be able to decompress it. Any ideas?


A:

I had the same problem. I found the solution here:
http://www.pymotw.com/2/lzma/index.html#module-lzma
<code>import lzma
from cStringIO import StringIO

s = StringIO(data)
lzc = lzma.LZMACompressor()
lzd = lzma.LZMADecompressor()

compressed = lzc.compress(data)
compressed += lzc.flush()

decompressed = lzd.decompress(compressed)
</code>

