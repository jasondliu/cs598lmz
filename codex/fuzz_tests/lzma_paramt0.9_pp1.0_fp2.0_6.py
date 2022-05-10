from lzma import LZMADecompressor
LZMADecompressor().decompress(b)
</code>


A:

I was getting an error doing the same thing, and found this which works for me. From the comments it explains why:
<code>import lzma
str = lzma.open(filename, "r", encoding='utf8').read()
print(str)
</code>

