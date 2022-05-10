import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))
libc = ctypes.cdll.LoadLibrary("libc.so.6")
libc.rand.restype = ctypes.c_int
libc.rand()
randint = FUNTYPE(libc.rand)
r = randint(pointer(c_int(1)))
r = randint(pointer(c_int(1)))
r = randint(pointer(c_int(1)))
print(r)
