from bz2 import BZ2Decompressor
BZ2Decompressor().__doc__

'BZ2Decompressor() -> decompressor object\n\nCreate a new decompressor object. This object may be used to decompress\nBZ2-compressed data.\n\n'




>>> import bz2
>>> bz2.decompress(bz2.compress(data)) == data
True


>>> bz2.compress(data)
b'BZh91AY&SY\xed\x88\x1a\\F\x00\x00o\x00\x00\x01\x00\x18\x00\x01\x00{$\xd6\x92\xbc\xf0\xe0\xe7\x02\x00p\x00\x00\x00\xe2\x84Zh\x1e\x0c'



>>> bz2.compress(data * 2)
b'BZh91AY&SY\xed\x88\x1a\\F\x00\x00o\x00\x00\x01\x
