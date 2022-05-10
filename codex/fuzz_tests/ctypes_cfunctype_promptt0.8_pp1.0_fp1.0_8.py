import ctypes
# Test ctypes.CFUNCTYPE
c_double_p = ctypes.POINTER(ctypes.c_double)
c_double2_t = ctypes.CFUNCTYPE(ctypes.c_double,
                               ctypes.c_double, ctypes.c_double)

print("Testing ctypes.CFUNCTYPE")
for i in range(10):
    f = c_double2_t(lambda x, y: x * y)
    a = numpy.asarray(range(i + 1) * 2, dtype='d').reshape((i + 1, 2))
    b = numpy.empty(i + 1, dtype='d')
    f(a, b)
    assert_equal(a[:, 0] * a[:, 1], b)


# Test ctypes.PYFUNCTYPE
print("Testing ctypes.PYFUNCTYPE")
py_f = ctypes.PYFUNCTYPE(ctypes.py_object, ctypes.py_object)

for i in range(10):
    f = py_f(lambda
