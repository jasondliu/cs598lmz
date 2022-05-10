from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# bz2.open()
with bz2.open('sample.bz2', 'rt') as f:
    text = f.read()

# compresslevel=9
compressed = bz2.compress(data, compresslevel=9)


# lzma
import lzma
with lzma.open('sample.xz', 'rt') as f:
    text = f.read()

with lzma.open('sample.xz', 'wt') as f:
    f.write(text)

# compresslevel=9
compressed = lzma.compress(data, format=lzma.FORMAT_XZ, check=lzma.CHECK_SHA256, compresslevel=9)

# lzma.LZMADecompressor().decompress(data)
# lzma.open()
