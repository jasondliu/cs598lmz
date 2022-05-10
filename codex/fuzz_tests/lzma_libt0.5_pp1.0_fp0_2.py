import lzma
lzma.decompress(z)

#%%
import gzip
gzip.decompress(z)

#%%
import bz2
bz2.decompress(z)

#%%
import lz4
lz4.decompress(z)

#%%
import lz4.frame
lz4.frame.decompress(z)

#%%
import lz4.block
lz4.block.decompress(z)

#%%
import zlib
zlib.decompress(z)

#%%
import brotli
brotli.decompress(z)

#%%
import zstandard
zstandard.ZstdDecompressor().decompress(z)

#%%
import snappy
snappy.uncompress(z)

#%%
import xxhash
xxhash.xxh64(z).hexdigest()

#%%
import xxhash
xxhash.xxh32(z).hexdigest()

#%%
import xxhash
xxhash.xxh64(z
