import lzma
lzma.LZMACompressor().compress(b'foobar')

# Compress a file
import lzma
with open('data.out', 'wb') as f:
    compressor = lzma.LZMACompressor()
