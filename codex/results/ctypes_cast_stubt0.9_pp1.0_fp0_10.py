import ctypes
ctypes.cast(3j, ctypes.py_object)

# Descriptors
class A(object):
    def __init__(self):
         self._x = None
         self._thingy = None

    @property
    def thingy(self):
        return self._thingy

    @thingy.setter
    def thingy(self, value):
        self._thingy = value

    @thingy.deleter
    def thingy(self):
        del self._thingy

    def x(self):
        return self._x

    @property
    def x(self, value):
        self._x = value

    def _y(self, value=None):
        if value is None:
            return self._y
        else:
            self._y = value

    z = property(fget=lambda self: self._z)
    z = z.setter(lambda self, value: setattr(self, '_z', value))
    z = z.deleter(lambda self: delattr(self, '_z'))

    z = z.set
