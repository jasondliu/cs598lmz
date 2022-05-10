import ctypes
ctypes.cast(id(0), ctypes.py_object).value

class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

from weakref import WeakKeyDictionary

class Car(object):
    def __init__(self, model, parts):
        self.model = model
        self.parts = parts
        self._parts = WeakKeyDictionary()

    def add_part(self, part, quantity=1):
        self._parts[part] = quantity

    def __repr__(self):
        fmt = '{}({!r}, {!r})'
        return fmt.format(type(self).__name__, self.model, self.parts)

class Typed(object):
    expected_type = object
