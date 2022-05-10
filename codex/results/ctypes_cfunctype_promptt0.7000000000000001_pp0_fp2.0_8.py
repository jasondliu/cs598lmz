import ctypes
# Test ctypes.CFUNCTYPE(...)(...), ctypes.c_char_p(...), libc.printf
libc = ctypes.cdll.LoadLibrary("libc.so.6")

c_printf = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)(("printf", libc))
c_printf("Hello, %s!\n", ctypes.c_char_p("world"))

# Test ctypes.c_void_p(...), ctypes.cast(..., ...), ctypes.memmove(...),
# ctypes.py_object.from_address(...), ctypes.addressof(...)
buf = ctypes.create_string_buffer(4)
memmove = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t)(("memmove", libc))
memmove(buf, ctypes.c_void_p(id(buf)), ctypes.sizeof(ctypes.py
