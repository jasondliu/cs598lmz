import lzma
lzma.decompress(data)

# decompress data
import zlib
zlib.decompress(data)

# decompress data
import bz2
bz2.decompress(data)

# decompress data
import lz4
lz4.decompress(data)

# decompress data
import snappy
snappy.decompress(data)

# decompress data
import brotli
brotli.decompress(data)

# decompress data
import zstandard
zstandard.ZstdDecompressor().decompress(data)

# decompress data
import blosc
blosc.decompress(data)

# decompress data
import zopfli
zopfli.decompress(data)

# decompress data
import zopfli.zlib
zopfli.zlib.decompress(data)

# decompress data
import zopfli.gzip
zopfli.gzip.decompress(data)

# decompress data
import zopfl
