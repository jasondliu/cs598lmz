import ctypes
# Test ctypes.CField

################################################################
#
# Bug #2046
# http://sourceforge.net/tracker/?func=detail&atid=105470&aid=2046&group_id=5470
#
# The ctypes.CField should be able to handle bitfields
#
################################################################

import ctypes

class BITFIELD(ctypes.Structure):
    _fields_ = [
        ("bit_one", ctypes.c_uint32, 1),
        ("bit_two", ctypes.c_uint32, 1),
        ("bit_three", ctypes.c_uint32, 1),
        ("bit_four", ctypes.c_uint32, 1),
        ("bit_five", ctypes.c_uint32, 1),
        ("bit_six", ctypes.c_uint32, 1),
        ("bit_seven", ctypes.c_uint32, 1),
        ("bit_eight", ctypes.c_uint32, 1),

        ("bit_nine", ctypes.c_uint32, 1),
        ("bit_ten", ctypes.c
