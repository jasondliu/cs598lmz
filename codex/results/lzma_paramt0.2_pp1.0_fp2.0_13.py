from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# lzma.LZMAError: Input format not supported by decoder
</code>
I'm not sure what I'm doing wrong. I'm using Python 3.7.0.


A:

The <code>LZMADecompressor</code> class is not the same as the <code>lzma</code> module. The <code>lzma</code> module is a wrapper around the liblzma library. The <code>LZMADecompressor</code> class is a wrapper around the <code>lzma</code> module.
The <code>lzma</code> module has a <code>decompress</code> function that can be used to decompress data that was compressed with the <code>lzma</code> module.
<code>from lzma import decompress
decompress(data)
</code>

