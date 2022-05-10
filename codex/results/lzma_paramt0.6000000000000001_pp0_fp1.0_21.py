from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

#%%
# to compress
import lzma
lzma.compress(data)
lzma.decompress(data)

#%%
# to compress
import bz2
bz2.compress(data)
bz2.decompress(data)

#%%
# to compress
import zlib
zlib.compress(data)
zlib.decompress(data)

#%%
# to compress
import brotli
brotli.compress(data)
brotli.decompress(data)

#%%
# to compress
import snappy
snappy.compress(data)
snappy.decompress(data)

#%%
# to compress
import lz4.block
lz4.block.compress(data)
lz4.block.decompress(data)

#%%
# to compress
import zstd
zstd.compress(data)
zstd.decompress(data)

#%%
# to compress
import blosc
bl
