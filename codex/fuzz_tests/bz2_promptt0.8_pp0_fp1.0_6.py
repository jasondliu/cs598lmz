import bz2
# Test BZ2Decompressor
# data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# bz_decompressor = BZ2Decompressor()
#
# try:
#     print(bz_decompressor.decompress(data))
#     print(bz_decompressor.flush())
# except EOFError:
#     print('End of compressed data')
#


# Test BZ2Compressor
uncompressed_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

