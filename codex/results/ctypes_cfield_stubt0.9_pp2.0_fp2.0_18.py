import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CPointerType = type(ctypes.c_int.in_dll)

class P(ctypes.CField):
    _type_ = 'L'
ctypes.P = P

def struct_getattr(self, name):
    field = None
    try:
        field = getattr(self, '_type_')._fields_[name]
    except KeyError:
        pass
    if isinstance(field, P):
        obj = self._type_()
        ctypes.memmove(ctypes.addressof(obj), ctypes.addressof(self),
                       ctypes.sizeof(self))
        return obj
    elif isinstance(field, ctypes.CField):
        if isinstance(field._type_, str):
            tp = getattr(ctypes, 'c_' + field._type_)
            return tp.in_dll(self, name)
        else:
            obj = field._type_()
            ctypes.memmove(ctypes.addressof(obj), ctypes.add
