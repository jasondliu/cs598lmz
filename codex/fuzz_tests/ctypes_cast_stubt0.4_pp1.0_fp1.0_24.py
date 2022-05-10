import ctypes
ctypes.cast(ctypes.pointer(ctypes.c_int(10)), ctypes.POINTER(ctypes.c_float))

# ctypes.cast(ctypes.pointer(ctypes.c_int(10)), ctypes.POINTER(ctypes.c_float))
# Out[122]: <__main__.LP_c_float at 0x7f2d3c4c4f80>

# ctypes.cast(ctypes.pointer(ctypes.c_int(10)), ctypes.POINTER(ctypes.c_float)).contents
# Out[123]: c_float(10.0)

# ctypes.cast(ctypes.pointer(ctypes.c_int(10)), ctypes.POINTER(ctypes.c_float)).contents.value
# Out[124]: 10.0

# ctypes.cast(ctypes.pointer(ctypes.c_int(10)), ctypes.POINTER(ctypes.c_float)).contents.value = 11
# ctypes.cast(ctypes.pointer(ctypes.c_int(10)), c
