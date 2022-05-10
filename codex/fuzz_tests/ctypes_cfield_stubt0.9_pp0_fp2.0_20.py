import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

ctypes.CField.__repr__ = lambda self: "CField(%s)" % self._name

def reprptr(self):
    return "<LP_%r instance at 0x%x>" % (self._type_, id(self))
ctypes._pointer_type_cache[ctypes._c_void_p.__ctype_le__] = (None, ctypes._c_void_p, None)
ctypes._pointer_type_cache[ctypes._c_void_p].__repr__ = reprptr

ctypes.c_uint8 = ctypes.c_ubyte
ctypes.c_uint16 = ctypes.c_ushort
ctypes.c_uint32 = ctypes.c_uint
ctypes.c_int8 = ctypes.c_byte
ctypes.c_int16 = ctypes.c_short
ctypes.c_int32 = ctypes.c_int
ctypes.c_int64 = ctypes.c_longlong
ctypes.c_uint64 = ctypes.c_ulonglong
