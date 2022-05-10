from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

import bz2
bz2_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
bz2.decompress(bz2_data)

import zlib
zlib.decompress(b'x\x9cK\xcb\xcf\x07\r\x00\x02\xa2\xe5\x02\x00+\xc8\xcfMJH\xc9\xccK\xe5\x02')

# Compression
import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)

import bz2
t = b
