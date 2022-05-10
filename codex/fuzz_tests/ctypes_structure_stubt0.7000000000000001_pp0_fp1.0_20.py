import ctypes

class S(ctypes.Structure):
    x = ctypes.c_size_t
    p = ctypes.POINTER(ctypes.c_size_t)

# ctypes.sizeof(ctypes.c_size_t) = ctypes.sizeof(ctypes.POINTER(ctypes.c_size_t))
# so we must create one based on the underlying type.
ctypes.c_ssize_t = ctypes.c_longlong if ctypes.sizeof(ctypes.c_void_p) == 8 else ctypes.c_long

class S2(ctypes.Structure):
    x = ctypes.c_ssize_t
    p = ctypes.POINTER(ctypes.c_ssize_t)

# cast from our new type to ctypes.c_size_t
S2_cast = S2.from_address(ctypes.addressof(S().p))
print(ctypes.sizeof(S2_cast))
print(ctypes.sizeof(S().p))

# cast from ctypes.c_size_t to our new type
S
