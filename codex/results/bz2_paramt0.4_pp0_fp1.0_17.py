from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2data)

# bz2data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# print(bz2.decompress(bz2data))

# import gzip
# s = b'witch which has which witches wrist watch'
# print(len(s))
# t = gzip.compress(s)
# print(len(t))
# print(gzip.decompress(t))
# print(gzip.compress(s))
#
# f = gzip.open('/Users/michael/myfile.txt.gz', 'wb')
# f.write(s)
# f.close()
#
# import gzip
# f = gzip.open('/Users/michael/myfile.txt
