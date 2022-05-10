import lzma
lzma.LZMADecompressor._decompressor.decompress = lzma.decompress

decomp_obj = lzma.LZMADecompressor()

with open("lzma_data.txt", "rb") as f:
    data = f.read()

decompressed_data = decomp_obj.decompress(data)
print(decompressed_data)
</code>
The following solution also fails for the same reason: Python lzma file compression and decompression
and so far, I haven't found any other way to uncompress a compressed bytestream using lzma from Python 3.


A:

If you have lzma installed, use this to uncompress:
<code>import lzma
with lzma.open("lzma_data.txt") as f:
    output = f.read()
</code>

