import bz2
# Test BZ2Decompressor
bzdecomp = bz2.BZ2Decompressor()
ret = bzdecomp.decompress(b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")
print(ret)

# Test BZ2Compressor
bzcomp = bz2.BZ2Compressor()
ret = bzcomp.compress(b"this   is a string to bz2 compress")
ret += bzcomp.flush()
print(ret)

import re
print(re.findall(r"\w+day\b", "Sunday Monday Tuesday Wednesday Thursday Friday Saturday"))

import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.dec
