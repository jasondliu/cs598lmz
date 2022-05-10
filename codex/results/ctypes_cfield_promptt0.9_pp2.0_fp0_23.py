import ctypes
# Test ctypes.CField
class CFields(ctypes.Structure):
    _fields_ = [("a", ctypes.c_byte),
                ("b", ctypes.c_char),
                ("c", ctypes.c_ubyte),
                ("d", ctypes.c_short),
                ("e", ctypes.c_ushort),
                ("f", ctypes.c_int),
                ("g", ctypes.c_uint),
                ("h", ctypes.c_long),
                ("i", ctypes.c_ulong),
                ("j", ctypes.c_float),
                ("k", ctypes.c_double)
                ]

def test_cfield(x=CFields()):
    return (x.a, x.b, x.c, x.d, x.e, x.f, x.g, x.h, x.i, x.j, x.k)

def export_cfields():
    return CFields

# Test ctypes.SimpleType            
def test_c_char():
    return ctypes
