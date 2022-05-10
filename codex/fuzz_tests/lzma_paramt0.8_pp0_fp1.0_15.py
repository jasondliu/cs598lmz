from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_bytes)
#b'Python rules!'
</code>
And the <code>lzma</code> module has been builtin in Python 3.3 (source). Not sure what your environment is, but you may want to upgrade.

