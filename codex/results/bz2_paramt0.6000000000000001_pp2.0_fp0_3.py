from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

#3.3
from zlib import decompress
decompress(zlib_data)

#3.4
from base64 import b64decode
b64decode(b64data)

#3.5
from binascii import unhexlify
unhexlify(hex_data)

#3.6
from re import findall
findall("[A-Z]{4}",message)
''.join(findall("[A-Z]{4}",message))

#3.7
from struct import unpack
unpack('<I',message[:4])

#3.8
from itertools import product
''.join(chr(sum(bit << i for i, bit in enumerate(bits))) for bits in product(*[[0,1]]*8))

#3.9
from collections import Counter
c = Counter(message)
''.join(c.most_common()[-1])

#3.10
from itertools import compress
''.join(compress(message
