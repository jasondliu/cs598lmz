import lzma
lzma.LZMADecompressor().decompress(open('test.xz', 'rb').read())
</code>
This works in Python 2.7.3 and Python 3.2.3.

