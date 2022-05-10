import lzma
lzma.decompress(open('/tmp/foo.xz', 'rb').read())

#%%
import zlib
