import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.__module__ = 'ctypes'
ctypes.CField.__name__ = 'CField'

class CField_get(object):
    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return getattr(obj, self.name)

class CField_set(object):
    def __set__(self, obj, value):
        setattr(obj, self.name, value)

class CField_delete(object):
    def __delete__(self, obj):
        delattr(obj, self.name)

if sys.version_info[0] >= 3:
    import builtins
    exec('''def _cfield_get(self, obj, type=None):
        if obj is None:
            return self
        return getattr(obj, self.name)
def _cfield_set(self, obj, value):
    setattr(obj, self.name, value)
def _cfield_delete(self, obj):
    delattr(obj,
