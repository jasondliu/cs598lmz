from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# compressed_data = bz2.compress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
# print(compressed_data)
# print(bz2.decompress(compressed_data))

# import zlib
#
# s = b'witch which has which witches wrist watch'
# print(len(s))
#
# t = zlib.compress(s)
# print(len(t))
# print(t)
#
# print(zlib.decompress(t))
#
# print(zlib.crc32(s))

# from timeit import Timer
#
# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit
