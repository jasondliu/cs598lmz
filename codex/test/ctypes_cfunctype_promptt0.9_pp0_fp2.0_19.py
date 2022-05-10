import ctypes
# Test ctypes.CFUNCTYPE()
# This should work now on Mac OS X
from ctypes import c_int, c_void_p

opaqueS = ctypes.Structure

def prototype(*restype, **argtypes):
    return ctypes.CFUNCTYPE(restype, *argtypes.items())

def callback(*restype, **argtypes):
    return ctypes.CFUNCTYPE(restype, c_void_p, *argtypes.items())

NULL = lambda x: ctypes.cast(0, x)

def asptr(x, type):
    if isinstance(x, (int, long)):
        return ctypes.cast(x, type)
    return x



from ctypes import c_char_p, c_uint, c_uint32, c_uint8, c_ushort

# typedef uint8_t icmLuBase;
icmLuBase = c_uint8
# typedef uint32_t icmLuAlg;
icmLuAlg = c_uint
# typedef uint32_t icmLookup
