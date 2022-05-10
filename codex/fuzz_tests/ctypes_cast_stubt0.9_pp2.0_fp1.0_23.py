import ctypes
ctypes.cast(0, ctypes.py_object)
ctypes.pythonapi.PyCapsule_GetName.restype = ctypes.c_char_p
ctypes.pythonapi.PyCapsule_GetName.argtypes = [ctypes.py_object]
types = {'float32_t': 'float', 'float64_t': 'double'}
def cudatype(c): return types.get(ctypes.pythonapi.PyCapsule_GetName(c), ctypes.pythonapi.PyCapsule_GetName(c))

ctx = Context(devtype="cuda", device_id=0)
# numpy ndarrays
a = np.ones(5).astype(np.float32)
b = td.from_numpy(a)
type(b)  # ndarray.ndarray
b.raw  # cuda.device_array
b.data  # <Capsule object "float32_t *" at 0x7f5d48e469b0>
cudatype(b.data)  # float32
