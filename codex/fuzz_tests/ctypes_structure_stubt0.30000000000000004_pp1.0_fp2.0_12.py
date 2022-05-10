import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

# ctypes.addressof(s)
# ctypes.addressof(s.x)
# ctypes.addressof(s.y)

# ctypes.pointer(s)
# ctypes.pointer(s.x)
# ctypes.pointer(s.y)

# ctypes.byref(s)
# ctypes.byref(s.x)
# ctypes.byref(s.y)

# ctypes.cast(s, ctypes.c_void_p)
# ctypes.cast(s.x, ctypes.c_void_p)
# ctypes.cast(s.y, ctypes.c_void_p)

# ctypes.cast(s, ctypes.POINTER(S))
# ctypes.cast(s.x, ctypes.POINTER(ctypes.c_int))
# ctypes.cast(s.y, ctypes.PO
