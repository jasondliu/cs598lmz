from lzma import LZMADecompressor
LZMADecompressor().decompress(bytearray(LZMAFILE))
</code>
This returns a <code>b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00...'</code> type object.
How do I convert this to a string?


A:

You can just call <code>decode</code> on the returned byte array to convert it to a string.
<code>LZMADecompressor().decompress(bytearray(LZMAFILE)).decode()
</code>
Edit:
You'll need to specify the encoding as well. I'm guessing it's <code>utf-8</code> but it could be something else.

