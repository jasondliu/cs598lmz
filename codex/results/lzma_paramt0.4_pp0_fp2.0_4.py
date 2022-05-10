from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# Compress data
import lzma
data = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
with lzma.open('data.xz', 'w') as f:
    f.write(data)

# Decompress data
import lzma
with lzma.open('data.xz') as f:
    file_content = f.read()

# Compress data
import bz2
data = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
with bz2.open('data.bz2', 'w') as f:
    f.write(data)

# Decompress data
import bz2
with bz2.open('data.bz2') as f:
    file_content = f.read()

# Compress data
import zlib
data = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open('data.z', 'wb') as f:
    f.write(zlib
