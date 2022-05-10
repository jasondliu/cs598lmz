import lzma
lzma.decompress(encoded)

import bz2
decoded = bz2.decompress(encoded)
decoded

unicode(decoded, 'utf-8')

# Use lzma compression through the `lzma` module
import lzma
lzma.compress(raw)

# Decode the resulting bytes object
import lzma
lzma.decompress(encoded)

import lzma
unicode(lzma.decompress(encoded), 'utf-8')

# Import the `bz2` module
import bz2
bz2.decompress(encoded)

# Decode the resulting bytes object
import bz2
bz2.decompress(encoded)

import bz2
unicode(bz2.decompress(encoded), 'utf-8')

# Import the `zlib` module
import zlib
zlib.decompress(encoded)

# Decode the resulting bytes object
import zlib
zlib.decompress(
