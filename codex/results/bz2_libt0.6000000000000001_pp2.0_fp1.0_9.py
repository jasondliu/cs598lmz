import bz2
bz2.open('somefile.bz2', 'wt')

# Output compression
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

# Input decompression
import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()

# BZ2Compressor and BZ2Decompressor
import bz2
compressor = bz2.BZ2Compressor()
decompressor = bz2.BZ2Decompressor()

compressed_data = compressor.compress(data)
compressed_data += compressor.flush()

data = decompressor.decompress(compressed_data)

# zlib
import zlib
s = zlib.compress(b'Hello World!')
zlib.decompress(s)

# LZMA
import lzma
s = lzma.compress(b'Hello World!')
s = lzma.decompress(s)

# Reading
