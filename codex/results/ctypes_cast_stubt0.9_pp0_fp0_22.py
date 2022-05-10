import ctypes
ctypes.cast(0x80000001, ctypes.c_void_p))

assert brk_platform_collision(edges,
ctypes.cast(0x80010000, ctypes.c_void_p),
ctypes.cast(0x80011000, ctypes.c_void_p))

assert brk_platform_collision(edges,
ctypes.cast(0x80018000, ctypes.c_void_p),
ctypes.cast(0x80018010, ctypes.c_void_p))

assert brk_platform_collision(edges,
ctypes.cast(0x80018014, ctypes.c_void_p),
ctypes.cast(0x80018084, ctypes.c_void_p))

assert brk_platform_collision(edges,
ctypes.cast(0x80018014, ctypes.c_void_p),
ctypes.cast(0x83000000, ctypes.c_void_p))

assert brk_platform_collision(edges,
ctypes
