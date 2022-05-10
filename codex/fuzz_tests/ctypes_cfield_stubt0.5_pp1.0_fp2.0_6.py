import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_c_field_instance():
    assert S.x.__class__ is ctypes.CField
    assert S.x.__class__.__name__ == 'CField'
    assert S.x.__class__.__module__ == 'ctypes'
    assert S.x.__class__.__bases__ == (ctypes.Field,)
    assert S.x.__class__.__doc__ == 'CField(name, type, offset) -> Field'
    assert S.x.__class__.__dict__['__module__'] == 'ctypes'
    assert S.x.__class__.__dict__['__name__'] == 'CField'
    assert S.x.__class__.__dict__['__qualname__'] == 'CField'
    assert S.x.__class__.__dict__['__doc__'] == 'CField(name, type, offset) -> Field'
    assert S.x.__class__.__dict__['__init__'] is ctypes.Field.__init__
    assert S.x
