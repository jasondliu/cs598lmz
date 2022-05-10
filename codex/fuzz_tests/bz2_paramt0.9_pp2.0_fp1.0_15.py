from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(FD.read())
</code>

It decompress the data. So, to get back the compressed data. You'll need to compress it by compressing the decompressed data (don't run the compression, if you still need to keep them compressed).

<code>from bz2 import BZ2Compressor
compressed = BZ2Compressor().compress(BZ2Decompressor().decompress(FD.read()))
</code>

