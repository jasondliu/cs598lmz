from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self, n: b''
</code>

