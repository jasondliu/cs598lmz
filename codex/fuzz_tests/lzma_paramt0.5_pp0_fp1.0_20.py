from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

import bz2
bz2_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
bz2.decompress(bz2_data)

with gzip.open('example.txt.gz', 'rt') as input:
    text = input.read()

with bz2.open('example.txt.bz2', 'rt') as input:
    text = input.read()

with lzma.open('example.txt.xz', 'rt') as input:
    text = input.read()

# 14.11.2.2. Compressing and Decompressing Data in Memory
import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = z
