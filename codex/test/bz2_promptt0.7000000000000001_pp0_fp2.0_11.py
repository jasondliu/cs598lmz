import bz2
# Test BZ2Decompressor with a huge number of small input chunks.
# This helps find cases where the decompressor isn't updating its
# internal state after each chunk.  In particular, this uncovered
# a bug in 2.5.2's zlibmodule.c.
CHUNK_SIZE = 100
REPEATS = 1000
data = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
compressor = bz2.BZ2Compressor()
bigdata = data * REPEATS
