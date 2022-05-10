from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# print(bz2.decompress(bz2_data))

# from bz2 import BZ2Decompressor
# decompressor = BZ2Decompressor()
# decompressor.decompress(bz2_data)
# decompressor.decompress(b'\x00\x00\x00\x07\x80M\x80\x00\x00\x00\r\x00\x00\x00')
# decompressor.flush()

# import bz2
# for line in bz2.BZ2File('file.bz2'):
#     print(line)

#
