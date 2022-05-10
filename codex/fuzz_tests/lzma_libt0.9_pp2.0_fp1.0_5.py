import lzma
lzma.decompress(bytes.fromhex("5d00078118000000"))

# IntToLE fails on big endian (just tried with Python 3.9)
lzma.decompress(bytes.fromhex("5d000781d0000000"))
# works on Linux 64-bit
lzma.decompress(bytes.fromhex("5d00078118000000"))

lzma.decompress(IntToLE(0x5d00078118000000, 8))
&gt; b'Hello '
</code>
so I can try to convert this number to little-endian before decompressing.
I want to make sure I didn't miss something about the algorithm before I ship this. The docs don't mention endianness of the uncompressed data. A few more questions:

does the algorithm produce variable-length output, or is it fixed-length, which I think would be easier to decompress in 8 hex-digit chunks?
is it possible to extract the original uncompressed data size without going through a decompression step?

Here is an example of that, where I set the <code>dict_size</
