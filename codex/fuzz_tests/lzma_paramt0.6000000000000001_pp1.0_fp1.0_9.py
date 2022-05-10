from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
# b'Hello World!Hello World!Hello World!Hello World!Hello World!'
</code>
As you can see, the compressed data is almost twice as large as the original data.

