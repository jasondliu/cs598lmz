import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CEnum(object):
    def __init__(self, enum_name, enum_values):
        self.values = {}

        for name, value in enum_values.items():
            globals()[name] = value
            self.values[name] = value


class CStruct(object):
    def __init__(self, struct_name, fields):
        self._fields = fields

class CUnion(CStruct):
    pass


# def Struct(self, name, fields):
#     return ctypes.Structure.__new__(ctypes.Structure)
