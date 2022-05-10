import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    """
    >>> C(1).x
    1
    >>> C().x += 1
    >>> C().x
    1
    >>> C().x = 2
    >>> C().x
    2
    """
    x = ctypes.c_int32(0)

class D(object):
    """
    >>> D(1).x
    1
    >>> D().x += 1
    >>> D().x
    1
    >>> D().x = 2
    >>> D().x
    2
    """
    _x = ctypes.c_int32(0)
    def _getx(self):
        return self._x.value
    def _setx(self, value):
        self._x.value = value
    x = property(_getx, _setx)

class E(object):
    """
    >>> E(1).x
    1
    >>> E().x += 1
    >>> E().x
    1
    >>> E().x = 2
    >>> E().x
    2
    """
   
