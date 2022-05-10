from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bytes('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))

# This is the string: b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

# The next problem is that the compressed file does not have the magic number b'BZ' at the start.
# So you have to use the BZ2Decompressor.decompress() method.

# bz2.BZ2Decompressor().decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x
