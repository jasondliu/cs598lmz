from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# lzma.LZMAError: Input format not supported by decoder
</code>
I'm using Python 3.6.4.
What am I doing wrong?


A:

The <code>lzma</code> module in Python 3.6 is a backport of the Python 3.3 <code>lzma</code> module. It does not support the <code>xz</code> format.
You can use the <code>backports.lzma</code> module instead, which does support <code>xz</code>.

