from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# lzma.LZMAError: Error -3 while decompressing data: invalid distance too far back
</code>
I am not sure if this is a bug in lzma.LZMADecompressor or in the Python implementation. I have tried this with Python 3.6.1 and 3.6.2.
I have also tried the same thing with the pylzma module and get the same error.
I have also tried this with Python 2.7.13 and get the same error.
I have also tried this with the xz command line tool and get the following output:
<code>$ xz -d -c &lt; test.lzma
xz: (stdin): Unexpected end of input
</code>
I have also tried this with the lzma command line tool and get the following output:
<code>$ lzma -d -c &lt; test.lzma
lzma: (stdin): Compressed data is corrupt
</code>
I have also tried this with the lzma-alone command line tool and get the following output
