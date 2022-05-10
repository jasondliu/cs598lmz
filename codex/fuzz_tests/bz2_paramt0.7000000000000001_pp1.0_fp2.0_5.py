from bz2 import BZ2Decompressor
BZ2Decompressor()._decompress

from bz2 import decompress
decompress(open('example.bz2', 'rb').read(), 9)

from bz2 import decompress
decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

from bz2 import decompress
decompress(b'BZh91A')

from bz2 import decompress
decompress(open('example.bz2', 'rb').read(), 9)

from bz2 import decompress
decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc
