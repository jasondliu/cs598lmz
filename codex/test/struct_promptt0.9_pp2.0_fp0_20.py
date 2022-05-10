import _struct
# Test _struct.Struct with all available size/alignment combinations.
# This is especially important on 64-bit machines.
import sys

class _TestBigEndian:
    # helper class for big-endian tests
    prefix = '>'
    getlong = lambda x,i: x[2*i] | (x[2*i+1] << 8)
    getlonglong = lambda x,i: x[4*i] | (x[4*i+1] << 8) | (x[4*i+2] << 16) | (x[4*i+3] << 24)

class _TestLittleEndian:
    # helper class for little-endian tests
    prefix = '<'
    getlong = lambda x,i: x[2*i+1] | (x[2*i] << 8)
    getlonglong = lambda x,i: x[4*i+3] | (x[4*i+2] << 8) | (x[4*i+1] << 16) | (x[4*i] << 24)

