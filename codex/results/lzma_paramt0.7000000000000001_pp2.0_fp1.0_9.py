from lzma import LZMADecompressor
LZMADecompressor.decompress(data)
</code>
However, unfortunately the <code>lzma</code> module doesn't support streaming decompression so it's not usable for my use case. I would like to know if there is any way to decompress the stream on the fly using a standard python module.


A:

This will be possible in Python 3.8, which adds a <code>LZMADecompressor.decompress_stream</code> method.

For earlier versions, you can use the backports.lzma module which provides the same API, but based on the liblzma library rather than the Python implementation.

<code>import backports.lzma as lzma

LZMADecompressor.decompress(data)
</code>

