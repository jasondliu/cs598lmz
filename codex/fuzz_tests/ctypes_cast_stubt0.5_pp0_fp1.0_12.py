import ctypes
ctypes.cast(a, ctypes.c_void_p)

a = np.arange(10)
ctypes.cast(a.ctypes.data, ctypes.c_void_p)

s = "Hello"
ctypes.cast(s, ctypes.c_void_p)

d = {'a': 1, 'b': 2}
ctypes.cast(d, ctypes.c_void_p)

l = [1, 2, 3]
ctypes.cast(l, ctypes.c_void_p)

t = (1, 2, 3)
ctypes.cast(t, ctypes.c_void_p)

ctypes.cast(1, ctypes.c_void_p)

ctypes.cast(None, ctypes.c_void_p)

ctypes.cast(np.arange(10), ctypes.c_void_p)

ctypes.cast(np.arange(10), ctypes.c_void_p)

ctypes.cast(np.arange(10), ctypes.
