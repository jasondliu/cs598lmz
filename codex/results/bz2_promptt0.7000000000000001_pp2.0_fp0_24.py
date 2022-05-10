import bz2
# Test BZ2Decompressor

d = bz2.BZ2Decompressor()

for b in bz2.decompress(b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084").split(b"\x00"):
    if len(b) > 0:
        print(b, d.decompress(b))

# BZh9 1AY&SY A
# 
# 
# 
# 
# 
# 
#  !
#
#
# Y
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

