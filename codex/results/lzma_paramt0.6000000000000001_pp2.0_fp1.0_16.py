from lzma import LZMADecompressor
LZMADecompressor.decompress(data)

#
# Exercise 7
#

from bz2 import BZ2Decompressor
bz2decomp = BZ2Decompressor()

bz2decomp.decompress(data)

#
# Exercise 8
#

from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

#
# Exercise 9
#

with open('data.txt') as f:
    data = f.read()

from base64 import b64decode

b64decode(data)

#
# Exercise 10
#

from base64 import b64decode

b64decode(data, altchars=b'$#')

#
# Exercise 11
#

import binascii

binascii.a2b_uu(data)

#
# Exercise 12
#

from base64 import b64encode

b64encode(data)

#
# Exercise 13
#

from base64 import b64
