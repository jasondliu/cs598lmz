import ctypes
# Test ctypes.CField.

ctypes.CField.__module__

try:
    ctypes.CField.s
except AttributeError:
    pass
else:
    print('AttributeError not raised')

class X(ctypes.Structure):
    _fields_ = [("s", ctypes.c_int)]

try:
    X.s
except AttributeError:
    print('AttributeError raised')
else:
    print('AttributeError not raised')

X._fields_[0].__module__

if hasattr(ctypes.CField, '__name__'):
    print(ctypes.CField.__name__)
