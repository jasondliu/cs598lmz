from lzma import LZMADecompressor
LZMADecompressor().decompress(dump_data)
</code>
<code>dump_data</code> contains a binary stream that is prefixed with a header. 
The binary looks 12 bytes long and it's version is 11.
I'm using Python 3.5.

