from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)
</code>
I get the following error:
<code>lzma.LZMAError: Input format not supported by decoder
</code>
I presume the reason is that <code>compressed_data</code> is not in the format expected by <code>LZMADecompressor</code>.
How can I decompress <code>compressed_data</code>?


A:

You're correct that the data is not in the format expected by <code>LZMADecompressor</code>.  The <code>LZMAInputStream</code> class from the <code>xz</code> library is able to read the data and decompress it, however:
<code>import xz

with xz.open('test.xz', 'rb') as f:
    decompressed_data = f.read()
</code>

