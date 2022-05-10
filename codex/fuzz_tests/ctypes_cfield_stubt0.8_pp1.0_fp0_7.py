import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class PyCType(CType):
    def __init__(self, ctype):
        self.ctype = ctype
        self.base = self._get_base(ctype)
        self.fields = self._get_fields(ctype)

    def _get_base(self, ctype):
        if ctype.__base__ is not object:
            return self._get_base(ctype.__base__)
        return ctype

    def _get_fields(self, ctype):
        fields = {}
        ffs = ctype._fields_
        if ffs is None:
            return fields
        for name, ftype in ffs:
            fields[name] = self._get_field(ftype)
        return fields

    def _get_field(self, ftype):
        if issubclass(ftype, ctypes.Structure):
            return PyCType(ftype)
        elif issubclass(ftype, ctypes.Array):
            return PyCType(ftype._type_)
        elif issubclass(
