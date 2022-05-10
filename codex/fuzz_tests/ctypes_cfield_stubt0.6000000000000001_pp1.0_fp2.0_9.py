import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __getitem__(self, index):
        return self.x[index]

# Test that the _fields_ list is copied
C._fields_.append(('y', ctypes.c_int))

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __getitem__(self, index):
        return self.x[index]
    def __setitem__(self, index, value):
        self.x[index] = value

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_long),
                ('z', ctypes.c_short),
                ('u', ctypes.c_char)]
    def __getitem__(self, index):
        return self.x[index]
    def __setitem__(self, index, value):
        self.x
