from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)
</code>
However, according to the docs this is only supported since Python 3.3.

