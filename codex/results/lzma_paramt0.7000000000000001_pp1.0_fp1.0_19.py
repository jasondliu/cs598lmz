from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
</code>
This will decompress the data I've shown in the question.
Is there a way to decompress the data without knowing the size of the uncompressed data prior to decompression?
I've looked at <code>xz</code>, but I can't make sense of the documentation.  It doesn't look like there's a way to do it, but I'm hoping I'm wrong.

