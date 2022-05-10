import ctypes
# Test ctypes.CFUNCTYPE by creating a ctypedef c_int(c_int) function pointer 
# type, and setting it to the same address as inc, below.
functype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
inc = functype(ctypes.addressof(functype.from_address(ctypes.addressof(inc))))

# Test that SetPointer() can be used to set a pointer that is a member of a 
# structure or union.

class POINTER_TEST(ctypes.Structure):
    _fields_ = [("p1", ctypes.POINTER(ctypes.c_int)),
                ("p2", ctypes.POINTER(ctypes.c_int)),
                ]
import sys
if sys.platform == 'win32':
    # On Windows, ctypes.POINTER(ctypes.c_int) and
    # ctypes.POINTER(ctypes.c_long) have the same typecode, and
    # ctypes.POINTER(ctypes.c_void_
