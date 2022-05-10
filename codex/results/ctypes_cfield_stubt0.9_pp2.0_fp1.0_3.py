import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# If a C type is already initialized with a Python value,
# '_objects' is a weakref:
assert type(S.x._objects) is normalized_weakref_proxy

# The attribute is set *before* the _objects weakref:
assert type(S.x._objects) is normalized_weakref_proxy

# Module level variables, class variables and instances:
# They get None:
assert type(__builtins__._objects) is normalized_weakref_proxy

mod = __import__('typestest4c')
assert type(mod.S.V._objects) is normalized_weakref_proxy

assert type(mod.S._objects) is normalized_weakref_proxy
s = mod.S()
assert type(s._objects) is normalized_weakref_proxy
s.V = mod.S()
assert type(s.V._objects) is normalized_weakref_proxy

a = mod.Array()
assert type(a._objects) is normalized_weakref_proxy
