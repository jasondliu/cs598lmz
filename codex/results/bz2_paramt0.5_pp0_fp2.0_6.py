from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

# bz2_decompress(compressed_data)

# uncompressed_data = bz2.decompress(compressed_data)
# print(uncompressed_data)

# import bz2
# data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# print(bz2.decompress(data))

# import bz2
# un = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
# print(bz2.decompress(
