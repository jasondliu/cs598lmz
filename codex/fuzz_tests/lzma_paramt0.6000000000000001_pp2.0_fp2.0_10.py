from lzma import LZMADecompressor
LZMADecompressor().decompress(file.read())
</code>
This will decompress the file. You can always use <code>file.tell()</code> to find out the current position.

