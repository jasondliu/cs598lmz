from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

#%%
from bz2 import BZ2Decompressor
bz2_decompressor = BZ2Decompressor()
result = bz2_decompressor.decompress(compressed_data)
result

#%%
bz2_decompressor.unused_data

#%%
bz2_decompressor = BZ2Decompressor()
more_data = bz2_decompressor.unused_data
result += bz2_decompressor.decompress(more_data)

#%%
result

#%%
bz2_decompressor.unused_data

#%%
bz2_decompressor = BZ2Decompressor()
result = bz2_decompressor.decompress(compressed_data)
result += bz2_decompressor.flush()

#%%
result

#%%
bz2_decompressor.unused_data

#%%
import bz2
bz2.decompress(compressed
