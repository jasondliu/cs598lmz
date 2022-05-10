import ctypes
# Test ctypes.CFUNCTYPE
cp = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
cp(lambda x: x+1, ctypes.c_int)(3)

cp = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
cp(lambda x, y: y.contents.value+1, ctypes.c_int, ctypes.POINTER(ctypes.c_int))(3, ctypes.pointer(ctypes.c_int(3)))
# Test ctypes.c_int
ctypes.c_int(1)
# Test ctypes.c_int*2
ctypes.c_int*2(1,2)
# Test ctypes.c_double
ctypes.c_double(1.0)
# Test ctypes.c_double*2
ctypes.c_double*2(1.0,2.0)
# Test ctypes.c_double.from_param
ctypes.c_double.from
