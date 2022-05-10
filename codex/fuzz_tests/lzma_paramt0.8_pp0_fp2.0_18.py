from lzma import LZMADecompressor
LZMADecompressor().decompress(s)
</code>
Now you could use <code>s.decode('latin-1')</code> to get the text, but it probably isn't going to make much sense, as the file is binary.

