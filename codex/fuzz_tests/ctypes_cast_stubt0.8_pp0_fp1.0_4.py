import ctypes
ctypes.cast(P, ctypes.POINTER(ctypes.c_float)).contents.value

x = np.array([1,2,3,4,5], dtype=np.float64)
x
x.ctypes.data
x.shape
x.ctypes.strides
data = x.ctypes.data
P = ctypes.cast(data, ctypes.POINTER(ctypes.c_double))
ctypes.cast(P, ctypes.POINTER(ctypes.c_double)).contents.value

for i in range(x.size):
    print(ctypes.cast(P + i, ctypes.POINTER(ctypes.c_double)).contents.value)

a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
a
#a.ctypes.data
#a.ctypes.strides
b = np.array([[11,12,13,14,15], [16,17,18,19,20]], dtype=np.float64)
b
