import ctypes
# Test ctypes.CField()

# XXX: we need to test the other flags as well
# XXX: we need to test the alignment as well
# XXX: we need to make sure that the int is of the correct size
# XXX: we need to test the offset as well

class Test(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ("c", ctypes.c_int),
        ("d", ctypes.c_int),
        ("e", ctypes.c_int),
        ("f", ctypes.c_int),
        ("g", ctypes.c_int),
        ("h", ctypes.c_int),
        ("i", ctypes.c_int),
        ("j", ctypes.c_int),
        ("k", ctypes.c_int),
        ("l", ctypes.c_int),
        ("m", ctypes.c_int),
        ("n", ctypes.c_int),
        ("o", ctypes.c_int),
       
