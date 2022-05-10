import lzma
lzma.decompress(data)

#bz2
import bz2
bz2.decompress(data)

#zlib
import zlib
zlib.decompress(data)

#brotli
import brotli
brotli.decompress(data)

#zstandard
import zstandard
ctx = zstandard.ZstdDecompressor()
ctx.decompress(data)

#snappy
import snappy
snappy.decompress(data)

#lz4
import lz4.frame
lz4.frame.decompress(data)

#lz4.block
import lz4.block
lz4.block.decompress(data)

#lz4.legacy
import lz4.legacy
lz4.legacy.decompress(data)

#lz4.stream
import lz4.stream
lz4.stream.decompress(data)

#lz4.frame.legacy
import lz4.frame.legacy

