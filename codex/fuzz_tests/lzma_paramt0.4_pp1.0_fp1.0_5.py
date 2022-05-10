from lzma import LZMADecompressor
LZMADecompressor().decompress(open(filename, 'rb').read()[12:])
</code>

