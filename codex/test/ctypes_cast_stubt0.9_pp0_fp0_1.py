import ctypes
ctypes.cast(0xdeadbeaf, ctypes.c_void_p).value

a = int("deadbeaf", 16)
