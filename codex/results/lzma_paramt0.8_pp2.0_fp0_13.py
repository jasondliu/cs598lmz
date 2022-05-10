from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_blob)
</code>
In a real program, you'd probably want to use a try/except block to catch exceptions that may be thrown by the decompressor.

