from lzma import LZMADecompressor
LZMADecompressor().decompress(open('/tmp/xz.lzma', 'rb').read())

# lzma.LZMAError: Input format not supported by decoder
</code>
I have tried to use <code>lzma</code> and <code>pyliblzma</code> but both of them failed.
How can I decompress a <code>.lzma</code> file in Python?


A:

You can use <code>lzma</code> module from <code>backports.lzma</code> package.
<code>from backports.lzma import LZMADecompressor
LZMADecompressor().decompress(open('/tmp/xz.lzma', 'rb').read())
</code>

