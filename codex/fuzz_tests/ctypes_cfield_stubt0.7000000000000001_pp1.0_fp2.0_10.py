import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFunc(ctypes.CFunctionType):
    def _make_instance(self, *args):
        return ctypes.CFuncPtr(self)

    def _make_funcptr(self, function):
        return ctypes.CFuncPtr(self, function)

    def _make_closure(self, function):
        return ctypes.CFuncPtr(self, function)

CFunctionType = CFunc

################################################################
#
# A minimal libffi. The functions here are adapted from the
# testsuite.

_FFI_OK = 0
_FFI_BAD_TYPEDEF = 1
_FFI_BAD_ABI = 2

class _FFI_TYPE_STRUCT(ctypes.Structure):
    _fields_ = [
        ('size', ctypes.c_size_t),
        ('alignment', ctypes.c_ushort),
        ('type', ctypes.c_ushort),
        ('elements', ctypes.POINTER(ctypes.c_void_p)),
    ]

class _FF
