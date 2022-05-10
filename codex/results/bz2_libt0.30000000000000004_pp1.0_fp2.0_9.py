import bz2
bz2.decompress(data)

# bz2.decompress(data)
# 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# >>> bz2.decompress(data)
# 'Wikipedia'
# >>> len(data)
# 25
# >>> len(bz2.decompress(data))
# 9

# >>> import bz2
# >>> bz2.decompress(data)
# 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# >>> b
