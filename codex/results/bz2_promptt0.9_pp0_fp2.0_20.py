import bz2
# Test BZ2Decompressor.
data = b'BZh91AY&SY.|\xc9\x90\xc0\x00\x00\x00\x04\x00\x1b\x00!\x9a'
decompressor = bz2.BZ2Decompressor()
data = decompressor.decompress(data)
data = decompressor.decompress(data)
data

decompressor.decompress(b'BZh91AY&SYA\xc8N\xc0\x00\x00\x01\x01\x80\x02\xc0 \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

decompressor.decompress(b'\xd8o\xa5*\x00\x10\x99\x00\x10RT\xc9\x04\x7f\x00\x00\x1a\x00!\x9ar\xdc\xc8\x04P')

decompressor.
