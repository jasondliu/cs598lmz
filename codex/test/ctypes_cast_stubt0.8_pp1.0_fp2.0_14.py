import ctypes
ctypes.cast(ctypes.cast(0, ctypes.POINTER(ctypes.c_int)), ctypes.c_void_p)

ctypes.cast(ctypes.cast(ctypes.cast(0, ctypes.POINTER(ctypes.c_int)), ctypes.c_void_p), ctypes.POINTER(ctypes.c_int))

p = ctypes.pointer(ctypes.c_int(1234))
p

p.contents

p1 = ctypes.cast(p, ctypes.POINTER(ctypes.c_char))
p1.contents

