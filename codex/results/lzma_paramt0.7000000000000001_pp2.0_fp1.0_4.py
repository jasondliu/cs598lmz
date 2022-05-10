from lzma import LZMADecompressor
LZMADecompressor().decompress(b'XZ\xfd\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00')
# b'Hello World!'
</code>
Note that the <code>lzma</code> module included with Python 3.3+ supports concatenated <code>.xz</code> files (and thus auto-detection of the end of the compressed data) without the need for a custom <code>decompress()</code> method.

