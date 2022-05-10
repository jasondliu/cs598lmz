import bz2
bz2.decompress(data)

#Gzip
import gzip
gzip.decompress(data)

#LZMA
import lzma
lzma.decompress(data)

#ZLIB
import zlib
zlib.decompress(data)

#Brotli
import brotli
brotli.decompress(data)

#LZ4
import lz4
lz4.frame.decompress(data)

#LZ4
import lz4
lz4.block.decompress(data)

#LZ4
import lz4
lz4.frame.decompress(data, uncompressed_size=1024)

#LZ4
import lz4
lz4.block.decompress(data, uncompressed_size=1024)

#LZ4
import lz4
lz4.frame.decompress(data, return_bytearray=True)

#LZ4
import lz4
lz4.block.decompress(data
