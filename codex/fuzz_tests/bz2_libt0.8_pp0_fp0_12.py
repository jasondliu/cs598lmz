import bz2
bz2.BZ2Decompressor().decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# or use command line bz2
print 'using command line to decompress'
import os
os.system('bzcat filename.bz2')

# bz2 compress a file
import bz2
uncompressed = 'The quick brown fox jumped over the lazy dog.'
comp = bz2.BZ2Compressor()
compressed = comp.compress(uncompressed)
compressed += comp.flush()
print compressed

# bz2 compress a file
import bz2
uncompressed = 'The quick brown fox jumped over the lazy dog.'
compressed = bz2.compress(uncompressed)
print compressed
