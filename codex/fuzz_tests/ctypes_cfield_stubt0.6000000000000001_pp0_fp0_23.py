import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(object):
    pass

ctypes.PyCField_Type = type(X.x)

class C(object):
    def __init__(self):
        self.x = ctypes.c_int()

X.x = property(lambda self: self._x, lambda self, value: setattr(self, "_x", value))

x = X()

# test that PyCField_Type has the same lifetime as it's underlying CField
x.x = C()
assert type(x.x).__name__ == 'CField'
assert isinstance(x.x, ctypes.CField)

x.x = None
assert type(x.x).__name__ == 'CField'
assert not isinstance(x.x, ctypes.CField)

del x
import gc
gc.collect()
assert not any(isinstance(obj, ctypes.CField) for obj in gc.get_objects())
