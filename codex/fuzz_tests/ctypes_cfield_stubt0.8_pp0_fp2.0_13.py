import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CStructure = S
ctypes.CUnion = S

class C(object):
    pointer = ctypes.c_int
    _fields_ = []

    def __new__(cls, *args, **kw):
        return cls.pointer.__new__(cls, *args, **kw)

    def __getattr__(self, attr):
        return self.value

    def __setattr__(self, attr, value):
        self.value = value

class c_int(C):
    _type_ = 'i'

class c_uint(C):
    _type_ = 'I'

class c_long(C):
    _type_ = 'l'

class c_ulong(C):
    _type_ = 'L'

class c_longlong(C):
    _type_ = 'q'

class c_ulonglong(C):
    _type_ = 'Q'

class c_float(C):
    _type_ = 'f'

class c_double
