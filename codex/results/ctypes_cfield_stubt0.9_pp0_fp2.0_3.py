import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

_get_resolved_type = {'inherit': lambda t, base: t,
                      'ctype': lambda t, base: t.type,
                      'CField': lambda t, base: t.subtype if base is type(t.subtype) else base}

class RecursiveTypeChecker:
    def __init__(self, type_: AnyType):
        self.type = type_

    def _resolve(self, base, array_level=None):
        if array_level:
            return array_level * [self.type.subtype.subshape[0]]
        return self._resolve(base, array_level=self.type.subshape[0])

    def _subtypes(self, base) -> List[AnyType]:
        first = base.subtype
        stacked = [base]

        while first != stacked[-1]:
            stacked.append(first)
            first = _get_resolved_type[type(first).__name__](first, base)
        return stacked

    def _bad_subtypes(self, base
