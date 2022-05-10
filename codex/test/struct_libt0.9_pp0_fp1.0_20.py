import _struct as struct
from scstruct import Struct

from xxtea_rand import make_rand_funcs
import xxtea
from lz1 import lz1_decompress
from xxtea_wrap import xxtea_decrypt_str, xxtea_decrypt_int, xxtea_decompress_int
from yrmm_decode import yrmm_decode
from scrt import scrt
from yuri_scrt import scrt4


# # stupidly slow!
"""
def inflate( data ):
    return zlib.decompress( data )


def deflate( data ):
    return zlib.compress( data )
"""

def inflate(data):
    from struct import unpack
    from zlib import decompress, MAX_WBITS

    pos = 0

    def read_byte():
        nonlocal pos
        b = data[pos]
        pos += 1
        return b

    def read_word():
        nonlocal pos
        b1 = data[pos + 0]
        b2 = data[pos + 1]

