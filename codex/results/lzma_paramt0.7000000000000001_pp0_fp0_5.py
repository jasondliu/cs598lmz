from lzma import LZMADecompressor
LZMADecompressor()
</code>
I'm trying to use <code>lzma</code> to decompress files I've downloaded from the internet for my own personal use. Here's the problem I'm running into.
The decompressor is not able to decompress a file properly. Here's the error I get:
<code>ValueError: LZMA (de)compressor requires exactly 1 argument
</code>
Here's the code I'm using:
<code>from lzma import LZMADecompressor
f = open('file.lzma', 'rb')
d = LZMADecompressor()
d.decompress(f.read())
</code>
Any suggestions?


A:

I figured it out. I needed to add the following code to the end:
<code>d.flush()
</code>

