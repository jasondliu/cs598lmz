from lzma import LZMADecompressor
LZMADecompressor().decompress(...)
</code>
Python 3.3 and above
<code>from lzma import open
open(..., format=lzma.FORMAT_XZ).read()
</code>

