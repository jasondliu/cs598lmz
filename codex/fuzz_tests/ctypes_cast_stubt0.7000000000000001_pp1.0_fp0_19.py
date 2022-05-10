import ctypes
ctypes.cast(None, ctypes.c_float)

# TODO: this raises an error under Python 2 and returns a type error under
# Python 3. Is this the desired behavior?
# ctypes.cast(None, ctypes.c_void_p)

ctypes.cast(None, ctypes.c_char_p)
ctypes.cast(None, ctypes.c_wchar_p)

ctypes.cast(None, ctypes.c_char)
ctypes.cast(None, ctypes.c_wchar)

ctypes.cast(None, ctypes.c_byte)
ctypes.cast(None, ctypes.c_ubyte)

ctypes.cast(None, ctypes.c_short)
ctypes.cast(None, ctypes.c_ushort)

ctypes.cast(None, ctypes.c_int)
ctypes.cast(None, ctypes.c_uint)

ctypes.cast(None, ctypes.c_long)
ctypes.cast(None, ctypes.c_ulong)


