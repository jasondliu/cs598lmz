from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

#%%
from lzma import LZMADecompressor
decompressor = LZMADecompressor()
decompressor.decompress(data)

#%%
from lzma import LZMADecompressor
decompressor = LZMADecompressor()
decompressor.decompress(data)
decompressor.unused_data

#%%
from lzma import LZMADecompressor
decompressor = LZMADecompressor()
decompressor.decompress(data)
decompressor.unused_data

#%%
from lzma import LZMADecompressor
decompressor = LZMADecompressor()
decompressor.decompress(data)
decompressor.unused_data
decompressor.decompress(decompressor.unused_data)

#%%
from lzma import LZMADecompressor
decompressor = LZMADecompressor()
decompressor.decompress(data
