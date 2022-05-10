import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int64
    y = ctypes.c_int64
    z = ctypes.c_int64

class _Mutable(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int64),
                ("y", ctypes.c_int64),
                ("z", ctypes.c_int64)]

class PyS(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int64),
                ("y", ctypes.c_int64),
                ("z", ctypes.c_int64)]

    @property
    def x(self):
        return self._x * 2

    @x.setter
    def x(self, v):
        self._x = v // 10

class MyObject(ctypes.c_int64):
    value = 0
    def __new__(cls, v):
        self = ctypes.c_int64.__new__(cls, v)
        self.value = v
        return self

    @property
   
