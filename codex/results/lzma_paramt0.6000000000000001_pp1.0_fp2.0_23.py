from lzma import LZMADecompressor
LZMADecompressor().decompress(bytes(compressed))

# Output:
# b'hello world!hello world!hello world!hello world!'
</code>

