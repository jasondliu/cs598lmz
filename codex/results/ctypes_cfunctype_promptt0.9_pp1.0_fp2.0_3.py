import ctypes
# Test ctypes.CFUNCTYPE() with Python object as input arg and
# return type.

import _ctypes_test

class PythonObj(object):
    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return "<value=%s>" % self.val

ReprFunc = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)

ffi_func = _ctypes_test.lib.get_repr_function()
repr = ReprFunc(ffi_func)

n = PythonObj(42)
m = repr(n)

print(n, m)
assert n.val == m.val

n = None
m = repr(n)
print(n, m)
assert n is None
assert m is None

n = 5
m = repr(n)
print(n, m)
assert n == m

n = 5.5
m = repr(n)
print(n, m)
assert n == m
"""
import _ctypes
