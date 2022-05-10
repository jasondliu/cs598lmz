from lzma import LZMADecompressor
LZMADecompressor.decompress(lzma_obj.compress(b"Stuff"))
b'Stuff'
</code>

