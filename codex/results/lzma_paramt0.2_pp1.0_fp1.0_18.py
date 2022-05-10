from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# lzma.LZMAError: Error -3 while decompressing data: invalid distance too far back
</code>
I'm not sure if this is a bug in the Python implementation of LZMA, or if the data is actually corrupt.

