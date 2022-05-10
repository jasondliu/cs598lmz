from lzma import LZMADecompressor
LZMADecompressor().decompress(open('compressed.lzma', 'rb').read())

# b'Hello World!'
</code>
Note that the <code>lzma</code> library is only available in Python 3.3 and higher.

