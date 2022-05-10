from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2.decompress
import bz2
bz2.decompress(bz2_data)

# lzma.decompress
import lzma
lzma.decompress(lzma_data)

# zlib.decompress
import zlib
zlib.decompress(zlib_data)

# zlib.decompressobj
import zlib
zlib.decompressobj().decompress(zlib_data)

# zstd.decompress
import zstd
zstd.decompress(zstd_data)

# zstd.ZstdDecompressor
import zstd
zstd.ZstdDecompressor().decompress(zstd_data)

# zstd.ZstdDecompressor.copy_stream
import zstd
zstd.ZstdDecompressor().copy_stream(BytesIO(zstd_data)).read()

# zstd.ZstdDecompressor.read_to_iter
import zstd
zstd
