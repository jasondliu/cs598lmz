from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x01')
# b'\x02'
</code>
<code>LZMACompressor</code> and <code>LZMADecompressor</code> are in the <code>lzma</code> module, but not in the <code>xz</code> module.
The LZMA module documentation is also a little more informative than the xz module documentation.

