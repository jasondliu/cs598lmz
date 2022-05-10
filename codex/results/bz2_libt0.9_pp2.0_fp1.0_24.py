import bz2
bz2.decompress(string)
</code>
However, bz2.decompress() makes a copy of the data and does not allow to use a callback or pointer to the compressed data, so it is not a valid option.
So the question is: how to decompress data at memory location <code>string</code> into memory location <code>out</code>?
Note: Since I am looking for in-place compression/decompression, I think using zlib is not a valid option, as it needs to create a temporary copy of the decompressed stream.


A:

you can use zlib and chop buffer into smaller pieces to avoid memory usage peak
<code>import zlib
uncompressed_data = bytearray()
compressed_data = your_memory_data
d = zlib.decompressobj()
while True:
    chunk = compressed_data[:1024]
    compressed_data = compressed_data[1024:]
    uncompressed_data.extend(d.decompress(chunk))
    if not compressed_data:
        break
uncompressed_data.extend(
