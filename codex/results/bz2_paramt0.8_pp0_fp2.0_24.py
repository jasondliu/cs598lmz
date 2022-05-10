from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# bz2
import bz2
un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
print(bz2.decompress(un))
print(bz2.decompress(pw))


# hex to b64
import binascii
msg = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f
