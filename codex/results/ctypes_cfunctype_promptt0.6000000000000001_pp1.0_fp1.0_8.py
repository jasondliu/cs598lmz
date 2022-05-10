import ctypes
# Test ctypes.CFUNCTYPE()
import _ctypes_test

################################################################
# Test the alignment of a field in a structure

# On x86-64, the alignment of short is 2, on x86 it is 1.
# To test this we create a structure with two shorts and one
# char, then we modify the value of the second short and check
# the value of the char.

class ShortStruct(ctypes.Structure):
    _fields_ = [("s1", ctypes.c_short),
                ("s2", ctypes.c_short),
                ("c", ctypes.c_char)]

ShortArray = ShortStruct * 3

sa = ShortArray()
sa[0].s1 = 0x1234
sa[0].s2 = 0x5678
sa[0].c = 0xFF
if (ctypes.sizeof(ctypes.c_short) == 2
    and ctypes.alignment(ctypes.c_short) == 2):
    # On x86-64, the alignment of short is 2, so the char is
    # at an address that is not a
