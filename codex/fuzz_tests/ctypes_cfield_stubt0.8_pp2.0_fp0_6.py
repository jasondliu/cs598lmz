import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A:
    def __getitem__(self, index):
        print(index)
        return 1

class Array1(ctypes.Structure):
    _fields_ = [
        ("value", ctypes.c_int),
        ("b", ctypes.c_double),
        ("p", ctypes.POINTER(ctypes.c_int)),
        ("a", ctypes.ARRAY(ctypes.c_int, 2))
    ]

    def __getitem__(self, index):
        return A()

    def __len__(self):
        return 5

    def func(self):
        pass

ctypes.Array = type(Array1.a)
ctypes.CPointer = type(Array1.p)

class Pointer1(ctypes.Structure):
    _fields_ = [
        ("value", ctypes.c_int),
        ("b", ctypes.c_double),
        ("p", ctypes.POINTER(ctypes.c_int)),
        ("a", ctypes.ARRAY(ctypes
