import bz2
# Test BZ2Decompressor
# decompressor = bz2.BZ2Decompressor()
# data = decompressor.decompress(compressed)
# print(data.decode('utf-8'))

# 2.6
# import bz2
# print(bz2.decompress(compressed))

# 2.7
# import bz2
# print(bz2.decompress(compressed).decode('utf-8'))

# 2.8
import bz2
print(bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))
