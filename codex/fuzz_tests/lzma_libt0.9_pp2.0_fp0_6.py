import lzma
lzma.decompress(data)

# Tool : gzip
import gzip
gzip.decompress(data)

import zlib
# Can decompress the gzip data directly
zlib.decompress(data)
# Get the size of the uncompressed data
zlib.decompress(data, 15+32)

# Tool : openssl
# https://www.python-forum.de/viewtopic.php?t=18673

# Tool : brotli
# https://www.baidu.com/link?url=QftXnvhlHAbI4n4YITv-efA_5m5n5pWG5n5zVGblXHBhBE-i6dWU0bYv6O2h6Mkl&wd=&eqid=cd36a1be00091b95000000065e2daaea

# Tool : zstd
# https://github.com/indygreg/python-zstandard
import zstd
data = zstd.decompressobj().decompress(read_data)

# Dis
