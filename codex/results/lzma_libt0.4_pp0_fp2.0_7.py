import lzma
lzma.decompress(data)

#bz2
import bz2
bz2.decompress(data)

#zlib
import zlib
zlib.decompress(data)

#lz4
import lz4.block
lz4.block.decompress(data)

#brotli
import brotli
brotli.decompress(data)

#lzf
import lzf
lzf.decompress(data)

#zstandard
import zstandard
zstd = zstandard.ZstdDecompressor()
zstd.decompress(data)

#snappy
import snappy
snappy.uncompress(data)

#blosc
import blosc
blosc.decompress(data)

#zopfli
import zopfli
zopfli.decompress(data)

#lz4framed
import lz4framed
lz4framed.decompress(data)

#lz4hc
import lz4
