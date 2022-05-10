from lzma import LZMADecompressor
LZMADecompressor()
</code>
And it works.
What is the reason of this warning?


A:

As documented (https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor.__init__), this warning means that the Decompressor object was created from an unsupported version of the XZ Utils (see https://tukaani.org/xz/).
You should update your XZ Utils to get rid of the warning.

