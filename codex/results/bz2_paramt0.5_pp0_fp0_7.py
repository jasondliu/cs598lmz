from bz2 import BZ2Decompressor
BZ2Decompressor()

from lzma import LZMADecompressor
LZMADecompressor()

from zlib import Decompresser
Decompresser()

from zlib import decompressobj
decompressobj()

from zlib import decompressobj
decompressobj(wbits=31)

from zlib import decompressobj
decompressobj(wbits=-15)

from zlib import decompressobj
decompressobj(wbits=15)

from zlib import decompressobj
decompressobj(wbits=47)

from zlib import decompressobj
decompressobj(wbits=31, zdict=b"")

from zlib import decompressobj
decompressobj(wbits=31, zdict=b"x")

from zlib import decompressobj
decompressobj(wbits=31, zdict=b"x"*32)

from zlib import decompressobj
decompressobj(wbits=31, zdict=b"x"*33)

from zlib import decompresso
