import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField._ctypes_ = True
CTypeLoader = ctypes.PyObj_FromPtr

# Additional type info
CTypeLoader.get_undefined_field = lambda x: 5
CTypeLoader.get_undefined_ptr = lambda x: 5
CTypeLoader.get_undefined_ptrarray = lambda x: 5
CTypeLoader.get_undefined_ctype = lambda x: 5

# How to fix a pointer with a given offset
CTypeLoader.ptr_with_fixed_address = lambda x, y, z: 5
CTypeLoader.size = 10

# The less object-oriented way...
class CStructLoader(CTypeLoader):
    def __setitem__(self, k, v):
        pass
    def __getitem__(self, k):
        return 5


class C(object):
    """A C-compatible structure"""
    def setup(self, value):
        self.value = value
    def __int__(self):
        return self.value
    def __float__(self):
        return float(self.value
