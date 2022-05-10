import bz2
bz2.decompress(bz2.compress(b'Hello World'))

import bz2
bz2.BZ2Compressor().compress(b'Hello World')

import bz2
bz2.BZ2Compressor().flush()

import bz2
compressor = bz2.BZ2Compressor()
compressor.compress(b'Hello World')
compressor.flush()

import bz2
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

import bz2
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b'BZh91AY&SY\x94
