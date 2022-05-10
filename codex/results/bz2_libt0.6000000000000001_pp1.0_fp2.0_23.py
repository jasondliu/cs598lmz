import bz2
bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# b'\x00\x00\x00\x07spam\x00\x08'
b'\x00\x00\x00\x07spam\x00\x08'.decode('utf-8')

# b'\x00\x00\x00\x07spam\x00\x08'
b'\x00\x00\x00\x07spam\x00\x08'.decode('utf-8', errors='ignore')


import zlib
s = b'witch which has which witches wrist watch'
len(s)
zlib.compress(s)
zlib.decompress(zlib.compress(s))
len(
