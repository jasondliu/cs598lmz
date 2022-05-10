from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
#
# bz2_decompressor = BZ2Decompressor()
#
# next_data = bz2_decompressor.decompress(bz2_data)
#
# while next_data:
#     print(next_data)
#     next_data = bz2_decompressor.unconsumed_tail
#     if next_data:
#         next_data = bz2_decompressor.decompress(next_data)
#
# print(bz2_decompressor.eof)
#
# bz2_data = b'BZh91AY&SY\x94$|
