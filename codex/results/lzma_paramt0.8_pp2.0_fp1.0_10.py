from lzma import LZMADecompressor
LZMADecompressor().decompress(open("data.xz", "rb").read())
</code>

