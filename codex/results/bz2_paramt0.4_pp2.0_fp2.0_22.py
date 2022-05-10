from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# bz2_decompressor = BZ2Decompressor()
# for data in [bz2_data[:4], bz2_data[4:12], bz2_data[12:]]:
#     try:
#         print(bz2_decompressor.decompress(data))
#     except EOFError:
#         print('EOFError')

# bz2_decompressor = BZ2Decompressor()
# print(bz2_decompressor.decompress(bz2_data))
# print(bz2_decompressor.decompress(b'BZh91AY
