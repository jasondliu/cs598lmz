from lzma import LZMADecompressor
LZMADecompressor().decompress(b).decode('utf-8')

#%%
from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b).decode('utf-8')

#%%
from lzma import LZMADecompressor
lzc = LZMADecompressor()
lzc.decompress(b)
#%%
lzc.decompress(b)
#%%
lzc.flush()
#%%
