from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")

# encoding: UTF-8
# Python 3
# http://www.pythonchallenge.com/pc/def/integrity.html

from bz2 import BZ2Decompressor
bz2_un = BZ2Decompressor().decompress(b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")
