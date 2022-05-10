import lzma
lzma.decompress(data)

#%%
import bz2
bz2.decompress(data)

#%%
import zlib
zlib.decompress(data)

#%%
import lz4.frame
lz4.frame.decompress(data)

#%%
import brotli
brotli.decompress(data)

#%%
import snappy
snappy.decompress(data)

#%%
import zstandard
zstandard.ZstdDecompressor().decompress(data)

#%%
import zopfli.zlib
zopfli.zlib.decompress(data)

#%%
import zopfli.gzip
zopfli.gzip.decompress(data)

#%%
import zopfli.deflate
zopfli.deflate.decompress(data)

#%%
import zopfli.lzma
zopfli.lzma.decompress(data)

#%%
import zopfl
