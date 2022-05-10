from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressedData)

#%%
from bz2 import decompress
decompress(compressedData)

#%%
from bz2 import BZ2Decompressor
decompressor = BZ2Decompressor()
decompressor.decompress(compressedData)

#%%
compressedData = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
decompressor = BZ2Decompressor()
decompressor.decompress(compressedData)

#%%
decompressor.decompress(b'\x00\x00\x00\x07\x80\x00\x10\x00')

#%%
compressedData = b'BZh91AY&SYA\xaf\x82\r\x00
