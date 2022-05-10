from lzma import LZMADecompressor
LZMADecompressor().decompress(...)
</code>
Though, if you're looking for a way to do it from within Numpy/Python, then you can use Zstd, which also has a Python binding:
<code>import zstd
zstd.decompress(...)
</code>

