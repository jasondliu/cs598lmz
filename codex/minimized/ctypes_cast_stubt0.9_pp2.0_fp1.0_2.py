import ctypes
seg = ctypes.c_void_p.from_address(0xDEADBEEF)
seg.value
