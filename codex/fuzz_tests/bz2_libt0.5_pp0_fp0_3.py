import bz2
bz2.decompress(bz2_compressed)

# Using the bz2 module
import bz2
un = "BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
pw = "BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"
print(bz2.decompress(un).decode('utf-8'))
print(bz2.decompress(pw).decode('utf-8'))

# Pickle
import pickle
pickle_compressed = b'\x80\x03]q\x00(
