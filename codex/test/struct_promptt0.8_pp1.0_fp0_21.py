import _struct
# Test _struct.Struct
import unittest
import sys, os, array

if sys.byteorder == 'little':
    schar      = 0x0102
    sint       = 0x03040506
    sfloat     = 0x0300785c
    sdouble    = 0x0300cc0d
    sldouble   = 0x0300f0e0d0b0a090
    sstring    = '\x01\x02\x03\x04'
else:
    schar      = 0x0201
    sint       = 0x05060403
    sfloat     = 0x003003e8
    sdouble    = 0x0dcc0003
    sldouble   = 0x908a0b0c0d0e0f03
    sstring    = '\x04\x03\x02\x01'

class _Test_Struct(unittest.TestCase):
    kinds = 'c s i f d l'.split()

