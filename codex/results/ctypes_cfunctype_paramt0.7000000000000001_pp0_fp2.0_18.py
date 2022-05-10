import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
print(FUNTYPE)
print(FUNTYPE(42))
print(FUNTYPE(42).__class__)
print(repr(FUNTYPE(42)))
print(FUNTYPE(42) + 2)
print(repr(FUNTYPE(42) + 2))
print(repr(FUNTYPE(42) + FUNTYPE(42)))
print(FUNTYPE(42)(1, 2))
print(FUNTYPE(42)(1, 2) + 1)
print(repr(FUNTYPE(42)(1, 2) + 1))
print(FUNTYPE(42)(1, 2) + FUNTYPE(42)(3, 4))

# ctypes.py_object, a special case
print(repr(ctypes.py_object() + ctypes.py_object()))

# Issue #6427: ctypes.wintypes.HANDLE.__repr__() does not work on Python 3
print(repr(ctypes.wintypes.HANDLE(-1)))
print(re
