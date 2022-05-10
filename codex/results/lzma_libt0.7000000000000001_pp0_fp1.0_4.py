import lzma
lzma.decompress()

# Compress data
lzma.compress(data)
lzma.compress(data, format=lzma.FORMAT_ALONE)
lzma.compress(data, format=lzma.FORMAT_XZ)

# Compress files
lzma.compress(fileobj)
lzma.compress(fileobj, format=lzma.FORMAT_ALONE)
lzma.compress(fileobj, format=lzma.FORMAT_XZ)

# Compress with filters
lzma.compress(data, check=lzma.CHECK_CRC64)
lzma.compress(data, preset=9)
lzma.compress(data, filters=[lzma.FILTER_LZMA2, dict(dict_size=4096)])
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_
