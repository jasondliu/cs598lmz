import ctypes
ctypes.cast(ctypes.byref(ctypes.c_int32(1)), ctypes.c_void_p)

# pointer to pointer
ctypes.cast(ctypes.byref(ctypes.c_longlong(1)), ctypes.POINTER(ctypes.c_longlong))

# cast a string to a c_char_p
c_char_p = ctypes.cast(b"aybabtu", ctypes.c_char_p)
print(c_char_p.value)

# cast a pointer to another type (no allocation)
c_char_p = ctypes.cast(ctypes.pointer(ctypes.c_longlong(1)), ctypes.POINTER(ctypes.c_int))
print(c_char_p[0])

# cast an array to a c_char
c_char_p = ctypes.cast(b"aybabtu", ctypes.c_char * 6)
print(ctypes.string_at(c_char_p))

# create a structure from a pointer
class St(ctypes.St
