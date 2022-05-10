from lzma import LZMADecompressor
LZMADecompressor().decompress(package)
</code>

As an aside, while this is likely to be the main cause of your problem, you may also have some problems with the size of the ZLIB stream.
The first byte in your <code>package</code> is <code>\x6f</code> (decimal 111).  The size of the stream happens to be a multiple of this, so there is no need for multiple concatorium.  However, it is possible for the stream size to be a little larger than the multiple of this number, in which case you need to add some to it.
The zlib specification says to add 1 more byte than is needed to fill up the concatorium, and set that byte to <code>\xff</code> (decimal 255).  So the standard says this, with the added <code>\xff</code> at the end:
<code>stream size 0x000051 ==81== number of 0xff needed 0x000051 &gt;0 times 00  
stream size 0x000052 ==82== number of 0xff needed 0x000052 &gt;0 times 00  
...  
stream size 0x0000
