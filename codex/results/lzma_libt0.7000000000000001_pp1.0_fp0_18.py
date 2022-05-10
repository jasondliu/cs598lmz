import lzma
lzma.LZMADecompressor().decompress(data)
 
# Output:
# b'Hello LZMA!'
</code>
<code>bz2.decompress()</code>:
<code>import bz2
bz2.decompress(data)
 
# Output:
# b'Hello BZ2!'
</code>
<code>zlib.decompress()</code>:
<code>import zlib
zlib.decompress(data)
 
# Output:
# b'Hello Zlib!'
</code>

