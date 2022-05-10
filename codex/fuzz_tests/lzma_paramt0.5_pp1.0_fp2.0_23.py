from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# bz2
import bz2
compressed_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
bz2.decompress(compressed_data)

# zlib
import zlib
compressed_data = b'x\x9c+\xcf\xcf\x07\x00\x00\x04\x04\x03'
zlib.decompress(compressed_data)

# gzip
import gzip
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
gzip.compress(s)
gzip.decompress(t)
