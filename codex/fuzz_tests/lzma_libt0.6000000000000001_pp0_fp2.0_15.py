import lzma
lzma.decompress(lzma.compress(b'hello, world'))

# Compress and decompress data using gzip
import gzip
s = b'Hello, world!'
t = gzip.compress(s)
gzip.decompress(t)

# Compress and decompress data using bz2
import bz2
t = bz2.compress(s)
bz2.decompress(t)

# Compress and decompress data using zlib
import zlib
t = zlib.compress(s)
zlib.decompress(t)

# Compress and decompress data using zstd
import zstd
t = zstd.compress(s)
zstd.decompress(t)
 
# Compress and decompress data using brotli
import brotli
t = brotli.compress(s)
brotli.decompress(t)

# Compress and decompress data using lz4
import lz4
t = lz4.frame.compress(s)
