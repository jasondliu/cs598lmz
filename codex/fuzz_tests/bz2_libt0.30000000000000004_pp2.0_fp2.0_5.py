import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# bz2.compress() returns a bytes object, and bz2.decompress() requires a bytes-like object.
# The easiest way to do this in Python 3 is to use the encoding argument to str.encode() to convert a string to bytes.

# bz2.BZ2Compressor and bz2.BZ2Decompressor objects let you stream data in and out without the entire compressed or decompressed data being held in memory at once.

import bz2
compressor = bz2.BZ2Compressor()
compressor.compress(b'Hello World!')
compressor.flush()

decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x
