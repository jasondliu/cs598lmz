import ctypes
ctypes.cast(ctypes.cast(c_int(1), ctypes.POINTER(ctypes.c_int)), ctypes.POINTER(ctypes.c_void_p)).contents.value

t2=time.time()
t12=t2-t1
print(t12)

t1=time.time()

for s in range(100000):
   ctypes.cast(ctypes.c_void_p(ctypes.cast(c_int(1), ctypes.POINTER(ctypes.c_int)).contents.value), ctypes.POINTER(ctypes.c_int)).contents.value

t2=time.time()
t22=t2-t1
print(t22)

t1=time.time()

for s in range(100000):
   ctypes.cast(ctypes.c_void_p(ctypes.c_int(1).value), ctypes.POINTER(ctypes.c_int))

t2=time.time()
t32=t2-t1
print(t32)
