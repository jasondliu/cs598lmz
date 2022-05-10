import ctypes
# Test ctypes.CField
class S:
    _fields_ = [('a', ctypes.CField)]
assert isinstance(S.a, ctypes.CField)
class S:
    _fields_ = [('a', ctypes.CField(ctypes.c_char))]
assert isinstance(S.a, ctypes.CField)
assert S.a.type is ctypes.c_char
try:
    class S:
        _fields_ = [('a', ctypes.CField('x'))]
except TypeError:
    pass
else:
    raise Exception

# This one is a bit of a special case, but we might as well test it
class S:
    _fields_ = [('a', ctypes.CField(None))]
assert isinstance(S.a, ctypes.CField)
assert not hasattr(S.a, 'type')

# Test ctypes.Union
class U(ctypes.Union):
    pass

class U(ctypes.Union):
    _fields_ = [('a', ctypes.c_int)]
assert U
