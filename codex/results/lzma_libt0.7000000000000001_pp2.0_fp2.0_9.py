import lzma
lzma.LZMADecompressor.decompress(files)
</code>
but it gives me a TypeError: 'str' does not support the buffer interface. I'm kind of lost here and I have no idea how to continue.
Any idea or suggestion?
Thank you in advance.


A:

This is a lzma compressed file, not a lzo compressed file. You can use lzma module to decompress it.

