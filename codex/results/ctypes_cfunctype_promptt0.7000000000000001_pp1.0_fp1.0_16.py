import ctypes
# Test ctypes.CFUNCTYPE
def py_add(a, b):
    print("py_add called with", a, b)
    return a + b

c_add = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(py_add)
ret = c_add(3, 5)
print("c_add returned", ret)

# Test ctypes.POINTER
class IntArray(ctypes.Structure):
    _fields_ = [("len", ctypes.c_int), ("values", ctypes.POINTER(ctypes.c_int))]

def py_fill_int_array(array):
    print("py_fill_int_array called with", array.len)
    for i in range(array.len):
        array.values[i] = i

c_fill_int_array = ctypes.CFUNCTYPE(None, ctypes.POINTER(IntArray))(py_fill_int_array)

data = IntArray(10, (ctypes.c_int * 10)
