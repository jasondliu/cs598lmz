from lzma import LZMADecompressor
LZMADecompressor().decompress( infile.read() )
</code>
That's one of the reasons I don't like Python's <code>zipfile</code> module very much.

