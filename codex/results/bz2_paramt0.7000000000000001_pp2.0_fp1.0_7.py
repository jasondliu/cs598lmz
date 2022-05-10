from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SY\xc4\x98\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# The first four bytes of the magic number are BZ, the next character is h, the digit is the block size in 100 kB, the next character is the compression mode, followed by two digits for the version number.
# You can decompress a bzip2 file in one line:
import bz2
un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00
