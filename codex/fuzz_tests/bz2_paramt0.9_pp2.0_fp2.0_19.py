from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(payload)

#jawnot found
import codecs
codecs.decode(payload, "rot-13")

#inflate and then xor
zlib.decompress(payload)
xor_str = codecs.decode(payload, "hex")
zlib.decompress(bytearray(ord(i[0]) ^ ord(i[1]) for i in zip(xor_str, xor_str)))

```
