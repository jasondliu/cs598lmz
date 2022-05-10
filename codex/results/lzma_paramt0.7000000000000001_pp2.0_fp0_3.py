from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# Compress
import lzma
with open('lorem.txt', 'rb') as input:
    with lzma.open('lorem.txt.xz', 'wt') as output:
        output.write(input.read())
"""

"""
# ZLIB
import zlib
s = b'witch which has which witches wrist watch'

# compress
t = zlib.compress(s)
# decompress
zlib.decompress(t)

# Compress
import zlib
with open('lorem.txt', 'rb') as input:
    with open('lorem.txt.z', 'wb') as output:
        output.write(zlib.compress(input.read()))

# Decompress
import zlib
with open('lorem.txt.z', 'rb') as input:
    with open('lorem.txt.decompress', 'wb') as output:
        output.write(zlib.decompress(input.read()))

# Compress with quality levels
import zlib
