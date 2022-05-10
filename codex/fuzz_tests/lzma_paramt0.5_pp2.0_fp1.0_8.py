from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# Decompress using the lzma module (requires Python 3.3 or later)
import lzma
lzma.decompress(data)

# Decompress using the backports.lzma module (for Python 2 and 3)
import backports.lzma
backports.lzma.decompress(data)

# Decompress using the pylzma module
import pylzma
pylzma.decompress(data)

# Decompress using the plzma module
import plzma
plzma.decompress(data)

# Decompress using the liblzma module
import liblzma
liblzma.decompress(data)

# Decompress using the lzmaffi module
import lzmaffi
lzmaffi.decompress(data)
