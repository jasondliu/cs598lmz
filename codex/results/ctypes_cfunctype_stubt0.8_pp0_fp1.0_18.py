import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return [1, 2, 3]

arr = np.zeros(shape=0, dtype=np.int64)
pybind11_demo.sum_array(arr, fun)
</code>

