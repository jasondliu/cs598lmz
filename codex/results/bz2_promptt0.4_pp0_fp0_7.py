import bz2
# Test BZ2Decompressor.eof

data = b'BZh91AY&SY\xd9b\xa4\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

decomp = bz2.BZ2Decompressor()
decomp.decompress(data)
decomp.eof

data = b'BZh91AY&SY\xd9b\xa4\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

decomp = bz2.BZ2Decompressor()
decomp.decompress(data)
decomp.eof

decomp.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
