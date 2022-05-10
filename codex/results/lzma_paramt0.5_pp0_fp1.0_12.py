from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# lzma.LZMAError: Input format not supported by decoder

# lzma.FORMAT_AUTO

from lzma import LZMADecompressor
LZMADecompressor(format=lzma.FORMAT_AUTO).decompress(data)

# b'Hello World'
</code>

