from bz2 import BZ2Decompressor
BZ2Decompressor()
from zlib import decompress
decompress(b'x\x9cK\xcaO\xcc\xce,M\xcd+\xcf/\xcaI,.Q(,R\x04\x00\x11\t$')
import zlib
from contextlib import closing
with closing(zlib.decompressobj()) as decompressor:
        decompressor.decompress(b'x\x9cK\xcaO\xcc\xce,M\xcd+\xcf/\xcaI,.Q(,R\x04\x00\x11\t$')
