from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# Compression
# As you can see, LZMA compression is slower than zlib and bz2, but it can
# achieve better compression ratios.

# The lzma module also supports the new XZ compression format. This is
# a newer, more efficient compression format supported by the xz utility.
# The difference between the two is similar to the difference between gzip
# and bzip2.

# The following example shows how to compress data using the new XZ
# compression format.

import lzma
compressed = lzma.compress(data)

# To decompress, you can use the LZMADecompressor class as before.

from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# The xz format supports additional options, such as setting the compression
# level. To do this, you need to use the XZCompressor class directly.

import lzma
compressor = lzma.XZCompressor(check=lzma.CHECK_
