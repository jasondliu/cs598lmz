from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# Block decompression
from lzma import LZMADecompressor
lzc = LZMADecompressor()
decompressed_data = lzc.decompress(data1)
decompressed_data += lzc.decompress(data2)
decompressed_data += lzc.decompress(data3)
lzc.unused_data

# Decompressing in streaming mode
from lzma import LZMADecompressor
lzc = LZMADecompressor()
lzc.decompress(data)
lzc.decompress(b'')  # returns the remaining data
lzc.decompress(b'x') # raises EOFError

# Compression
import lzma
with lzma.open('file.xz', 'w') as f:
    f.write(b'Hello World')

# Compression with options
import lzma
import io
bio = io.BytesIO()
with lzma.open(
