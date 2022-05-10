import ctypes
ctypes.cast(0, ctypes.py_object)

a = np.array([1,2,3])
a.dtype

a = np.array([1,2,3], dtype=np.float64)
a.dtype

a = np.array([1,2,3], dtype=np.int32)
a.dtype

np.zeros(10, dtype=np.int)

np.zeros((3,5), dtype=np.float)

np.ones((3,5), dtype=np.float)

np.full((3,5), 3.14)

np.arange(0, 20, 2)

np.linspace(0, 1, 5)

np.random.random((3,3))

np.random.normal(0, 1, (3,3))

np.random.randint(0, 10, (3,3))

np.eye(3)

np.empty(3)

np.ones(10) * 5

np.ones(10) *
