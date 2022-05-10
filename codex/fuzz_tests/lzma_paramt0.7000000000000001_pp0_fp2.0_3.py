from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self : b''
</code>
which I'm not thrilled about.

