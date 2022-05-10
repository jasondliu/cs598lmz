from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(message2[12:])

import binascii
binascii.unhexlify(b'686579206c6f72656d20756e6772616d')

from Crypto.Cipher import AES
key = b'YELLOW SUBMARINE'
cipher = AES.new(key, AES.MODE_ECB)
cipher.decrypt(b"hello world")
