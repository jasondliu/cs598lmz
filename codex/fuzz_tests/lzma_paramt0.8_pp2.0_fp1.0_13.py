from lzma import LZMADecompressor
LZMADecompressor().decompress(b"\x00\x00")
</code>
Calls to <code>decompress</code> can be chained, just like the <code>zlib</code> version.

