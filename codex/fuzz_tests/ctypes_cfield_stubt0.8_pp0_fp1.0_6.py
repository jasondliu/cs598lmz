import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CTypesBaseClass(BaseClass):
    ctype = None

    def _is_cfield(self, obj):
        return isinstance(obj, ctypes.CField)

    c_types = BaseClass._is_int, BaseClass._is_long, BaseClass._is_float, _is_cfield

    def __getitem__(self, index):
        from pypy.rpython.lltypesystem import lltype
        ctype = self.ctype
        if isinstance(index, slice):
            length = len(self)
            start, stop, step = index.indices(length)
            if step != 1:
                raise IndexError
            ptr = ctypes.cast(self.ctypes_data, ctypes.POINTER(ctype * length))
            return ptr.contents[start:stop]
        else:
            assert index >= 0
            ptr = ctypes.cast(self.ctypes_data, ctypes.POINTER(ctype))
            ptr = ctypes.POINTER(ctype)(ptr.contents, index)
            return
