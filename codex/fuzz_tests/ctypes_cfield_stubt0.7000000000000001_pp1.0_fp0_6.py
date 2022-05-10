import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Array(ctypes.Array):
    _type_ = ctypes.c_int

    def __getitem__(self, idx):
        return self.__dict__['_objects_'][idx]

class Array2(ctypes.Array):
    __getitem__ = Array.__getitem__
    __len__ = Array.__len__
    _type_ = ctypes.c_int

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int),
               ]

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int),
                ('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int),
               ]

class S4(ctypes
