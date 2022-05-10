from lzma import LZMADecompressor
LZMADecompressor().decompress(open('sample.txt', 'rb').read())
</code>
EDIT: This should work for both Python 2 and Python 3.  For Python 3, the accepted answer below makes LZMA available as a builtin, but under Python 2, you need to explicitly install it.

