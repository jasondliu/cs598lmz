from lzma import LZMADecompressor
LZMADecompressor().decompress(b'...')
</code>
If it's a zip file, use the built-in zipfile module.
If you know that the file is not compressed, then the built-in <code>open()</code> function will do.

