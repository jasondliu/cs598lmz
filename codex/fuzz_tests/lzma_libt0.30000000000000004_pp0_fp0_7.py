import lzma
lzma.decompress(compressed_data)

#bz2
import bz2
compressed_data = bz2.compress(data)
bz2.decompress(compressed_data)

#zlib
import zlib
compressed_data = zlib.compress(data)
zlib.decompress(compressed_data)

#gzip
import gzip
compressed_data = gzip.compress(data)
gzip.decompress(compressed_data)

#brotli
import brotli
compressed_data = brotli.compress(data)
brotli.decompress(compressed_data)

#lzf
import lzf
compressed_data = lzf.compress(data)
lzf.decompress(compressed_data)

#lz4
import lz4
compressed_data = lz4.compress(data)
lz4.decompress(compressed_data)

#zstd
import zstd
compressed
