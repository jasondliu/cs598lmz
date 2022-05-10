from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
</code>
That seems to work, but then my data is just .lzma files, so I'd be expecting to just call "lzma -d foo.lzma" or some equivalent.

