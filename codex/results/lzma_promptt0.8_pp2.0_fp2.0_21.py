import lzma
# Test LZMADecompressor by decompressing a short message encoded with LZMA.

compressed = b'\x5d\x00\x00\x80\x00\x10\x00\x00\x00\x03\x00\x03\x00\x04\x00\x00\x00\x00\x00\x11B$\x19\xd0\xb1@\xa8r]\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00'

decompressor = lzma.LZMADecompressor()
decompressor.decompress(compressed)

# b'Testing compression and decompression.'
</code>
It's the same string.


A:

<blockquote>
<p>If I use the same compressed string in Python 3 it doesn't work.</p>
