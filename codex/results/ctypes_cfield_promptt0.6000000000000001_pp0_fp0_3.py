import ctypes
# Test ctypes.CFields
class POINT(ctypes.Structure):
    _fields_ = (('x', ctypes.c_long),
                ('y', ctypes.c_long))

class RECT(ctypes.Structure):
    _fields_ = (('a', POINT),
                ('b', POINT))


# Test ctypes.GetSetClsAttr
class GetSetClsAttr(object):
    def __init__(self):
        self._attr = 1

    def _getattr(self):
        return self._attr

    def _setattr(self, value):
        self._attr = value

    attr = property(_getattr, _setattr)

# Test ctypes.GetSetDescr
class GetSetDescr(object):
    def __init__(self):
        self._attr = 1

    def _getattr(self, obj):
        return obj._attr

    def _setattr(self, obj, value):
        obj._attr = value

    attr = property(fget=_getattr, fset=_setattr)


