from lzma import LZMADecompressor
LZMADecompressor.decompress(data)
</code>
This will raise an <code>EOFError</code> if the data is truncated.

