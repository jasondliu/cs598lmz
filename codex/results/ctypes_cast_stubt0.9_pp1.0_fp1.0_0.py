import ctypes
ctypes.cast(ctypes.c_int(0x12345678), ctypes.POINTER(ctypes.c_char))

# prints: c_char_Array_4
print(ctypes.cast(ctypes.c_int(0x12345678), ctypes.POINTER(ctypes.c_char)))

ctypes.cast(ctypes.c_int(0x12345678),
            ctypes.POINTER(ctypes.c_char))[:]

print(ctypes.cast(ctypes.c_int(0x12345678), ctypes.POINTER(ctypes.c_char))[:])

# prints:
#b'\x78\x56\x34\x12'
print(ctypes.cast(ctypes.c_int(0x12345678),
                  ctypes.POINTER(ctypes.c_char))[:].tobytes())

ctypes.cast(ctypes.c_int(0x12345678), ctypes.POINTER(ctypes.c_char))[:] = b'\x23'

