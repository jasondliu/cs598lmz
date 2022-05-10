from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(file_contents)
</code>
Similarly, you can use <code>zlib.decompress(file_contents)</code> to decompress it if it is a <code>.gz</code> file.
If you are dealing with an <code>.xz</code> file:
<code>from lzma import LZMADecompressor
LZMADecompressor().decompress(file_contents)
</code>

