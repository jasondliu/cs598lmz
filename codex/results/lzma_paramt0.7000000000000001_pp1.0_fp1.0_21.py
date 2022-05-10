from lzma import LZMADecompressor
LZMADecompressor().decompress(compressedData)
</code>
I'm using Python 3.6.7.


A:

The problem is that the data that you have is not in the format that the <code>decompress</code> method expects. The <code>decompress</code> method expects to be passed data that was compressed using the LZMA algorithm (specifically, XZ) and is ready to be decompressed. The data that you have is not in this format.
There are two options:

Decompress the data yourself (this is not a trivial task), or
Find some sample code that already does this.

The second option is definitely easier. If you search for <code>decompress gzip</code>, you will find some.

