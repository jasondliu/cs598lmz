from lzma import LZMADecompressor
LZMADecompressor.decode(b"\xfd\x5d\xcb\x48\x01\x00\x00\x00\x00" + b"asdfghjkl")
</code>
I get the error
<code>lzma.LZMAError: Error -3 while decompressing data: invalid compressed data--length error
</code>
How do I fix this? I'm just trying to get the string <code>b'asdfghjkl'</code> as a result.


A:

I was able to accomplish this through the use of the lzma library.
<code>import lzma

data = b"\xfd\x5d\xcb\x48\x01\x00\x00\x00\x00" + b"asdfghjkl"

uncompressed = lzma.decompress(data)
print(uncompressed)
</code>

