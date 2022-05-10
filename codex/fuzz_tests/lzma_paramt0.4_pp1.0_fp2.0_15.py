from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# Compress data
import lzma
compressor = lzma.LZMACompressor()
compressor.compress(data)
compressor.flush()

# Compress data
import lzma
with lzma.open('file.xz', 'wt') as f:
    f.write(data)

# Decompress data
import lzma
with lzma.open('file.xz') as f:
    file_content = f.read()

# Compress data
import bz2
compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()

# Decompress data
import bz2
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(data)

# Compress data
import bz2
with bz2.open('file.bz2', 'wt') as f:
    f.write(data)

# Decompress data
import bz2
with b
