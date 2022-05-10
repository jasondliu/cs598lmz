from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# After lzma is installed, the following also works
import lzma
lzma.decompress(data)
</code>

