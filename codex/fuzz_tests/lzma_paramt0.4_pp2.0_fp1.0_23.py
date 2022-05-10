from lzma import LZMADecompressor
LZMADecompressor.decompress(data)

# LZMA/XZ compression
import lzma
with lzma.open('file.xz', 'wt') as f:
    f.write(text)

with lzma.open('file.xz', 'rt') as f:
    text = f.read()

# LZMA and XZ compression
import bz2
with bz2.open('file.bz2', 'wt') as f:
    f.write(text)

with bz2.open('file.bz2', 'rt') as f:
    text = f.read()

# bzip2 compression
import bz2
with bz2.open('file.bz2', 'wt') as f:
    f.write(text)

with bz2.open('file.bz2', 'rt') as f:
    text = f.read()

# bzip2 compression
import bz2
with bz2.open('file.bz2', 'wt') as f:
    f.write(
