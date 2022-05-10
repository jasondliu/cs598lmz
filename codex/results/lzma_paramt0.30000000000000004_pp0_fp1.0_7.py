from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# lzma.LZMAError: Input format not supported by decoder
</code>
I'm not sure what the problem is. I'm using Python 3.7.3 on Ubuntu 18.04.


A:

The problem is that the <code>LZMADecompressor</code> class does not support the format used by the <code>lzma</code> module.
The <code>lzma</code> module uses a custom format that is not compatible with the XZ format.
The <code>LZMADecompressor</code> class is only intended for the XZ format.

