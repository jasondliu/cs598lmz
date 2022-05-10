import bz2
bz2.decompress(bz2.compress(b"this is a test"))

#%%
import bz2
compressor = bz2.BZ2Compressor()
compressor.compress(b"this is a test")
compressor.flush()

#%%
import bz2
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(
    b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")
decompressor.decompress(b"\x00\x00\x00\x01\x01\x80")

#%%
import bz2
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(
    b"BZh91AY&SYA
