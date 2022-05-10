import lzma
lzma_decompress = lzma.decompress

from bitarray import bitarray
#from bitarray import bitarray
#import bitarray
import numpy as np
from numpy import int8
#import numpy


def decode_file(fin, int_type, fout):
    if int_type == int8:
        integer_size = 8
    elif int_type == uint8:
        integer_size = 8
    elif int_type == int16:
        integer_size = 16
    elif int_type == uint16:
        integer_size = 16
    elif int_type == int32:
        integer_size = 32
    elif int_type == uint32:
        integer_size = 32
    elif int_type == int64:
        integer_size = 64
    elif int_type == uint64:
        integer_size = 64
    else:
        raise Exception("Unknown integer type")


    bundle_bit_array = bitarray.bitarray()

    for i, row in enumerate(fin):
        if i
