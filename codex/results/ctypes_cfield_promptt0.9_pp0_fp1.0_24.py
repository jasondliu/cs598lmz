import ctypes
# Test ctypes.CField
libc = ctypes.cdll.msvcrt
class UDT(ctypes.Union):
    _pack_ = 1
    _fields_ = [("c1", ctypes.c_char),
                ("c2", ctypes.c_char)]
class struct_with_union(ctypes.Structure):
    _pack_ = 1
    _fields_ = [("i", ctypes.c_int),
                ("c", ctypes.c_char),
                ("u", UDT),
                ("ip", ctypes.c_void_p)]

%%python
import sys, ctypes

BUFSIZE = 8
# If python is compiled with gcc, the memory_order should be "mo_seq_cst"
memory_order = "mo_seq_cst"
byte_array_type = ctypes.c_ubyte * BUFSIZE
class AtomicULong(object):
    def __init__(self,*args):
        """
        Readable constructor. 
        Args are for setting the value of the AtomicULong
        """
        self
