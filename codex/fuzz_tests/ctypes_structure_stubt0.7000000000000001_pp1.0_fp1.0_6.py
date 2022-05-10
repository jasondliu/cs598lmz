import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong

ss = ctypes.cast(ctypes.pointer(S()), ctypes.c_void_p)
print ctypes.sizeof(S)
#print S.from_address(ctypes.addressof(ss) + 61)
print ss
print ss + 1
